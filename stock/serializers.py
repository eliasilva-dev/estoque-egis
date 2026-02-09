from rest_framework import serializers
from django.db import transaction
from collections import defaultdict
from invoice.models import Invoice
from stock.models import Stock, Item_category, Status_item, Locals, Equipament_type, Invoice_item
from movimentation.models import Movimentations, Movimentation_type
from invoice.serializers import ItemCatalogSerializer
from movimentation.rules import STATUS_TO_MOV_CODE

class EquipamamentTypeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Equipament_type
        fields = '__all__'





class ItemCategorySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Item_category
        fields = '__all__'


class StatusItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status_item
        fields = '__all__'


class LocalSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Locals
        fields = '__all__'



class StockListSerializer(serializers.ListSerializer):
    """
    Suporta many=True com:
    - Checagem de duplicados no payload (serial_number).
    - Validação de quantidade por Invoice_item (não exceder o restante).
    - bulk_create de Stock e bulk_create de Movimentations.
    - Atualização de Invoice_item.is_registred após o batch.
    """

    def _check_batch_duplicates(self, validated_data_list):
        serials = [d.get('serial_number') for d in validated_data_list if d.get('serial_number')]
        seen, dups = set(), set()
        for s in serials:
            if s in seen:
                dups.add(s)
            seen.add(s)
        if dups:
            raise serializers.ValidationError({
                'serial_number': [f'Número(s) de série duplicado(s) no payload: {", ".join(sorted(dups))}']
            })

    def _validate_invoice_item_remaining(self, validated_data_list):
        """
        Garante que o total enviado por item (Invoice_item) não exceda o restante.
        """
        sending_counts = defaultdict(int)
        for d in validated_data_list:
            item_obj = d.get('item')  # instância de Invoice_item
            if not item_obj:
                raise serializers.ValidationError({'item': ['Campo obrigatório.']})
            sending_counts[item_obj.id] += 1

        errors = {}
        # Usamos select_for_update para evitar condição de corrida dentro da transação
        for item_id, cnt in sending_counts.items():
            inv_item = Invoice_item.objects.select_for_update().get(pk=item_id)
            total_required = int(inv_item.quantity or 0)
            already_registered = Stock.objects.filter(item_id=item_id).count()
            remaining = total_required - already_registered
            if remaining <= 0:
                errors.setdefault('item', []).append(
                    f'O item da nota {item_id} já está totalmente registrado.'
                )
            elif cnt > remaining:
                errors.setdefault('item', []).append(
                    f'Para o item da nota {item_id}, você enviou {cnt}, mas faltam apenas {remaining}.'
                )

        if errors:
            raise serializers.ValidationError(errors)

    @transaction.atomic
    def create(self, validated_data_list):
        # 0) Checar duplicados internos
        self._check_batch_duplicates(validated_data_list)

        # 1) Validar contra Invoice_item.quantity (não exceder o restante)
        self._validate_invoice_item_remaining(validated_data_list)

        # 2) Criar Stock em lote
        stocks_to_create = [Stock(**item) for item in validated_data_list]
        created_stocks = Stock.objects.bulk_create(stocks_to_create)

        # 3) Criar Movimentations em lote
        request = self.context.get('request')
        user = getattr(request, 'user', None)
      
   

        movs_to_create = []

        mov_types = {
            mt.code: mt
            for mt in Movimentation_type.objects.all()
        }
        
        for stock, original_data in zip(created_stocks, validated_data_list):

            status_obj = original_data.get('status') 
            
            if not status_obj:
                raise serializers.ValidationError({
                    'status': ['Campo obrigatório.']
                })
            
            mov_code = STATUS_TO_MOV_CODE.get(status_obj.code)
            
            
            if not mov_code:
                raise serializers.ValidationError({
                    'status': [f'Status {status_obj.code} não possui movimentação associada.']
                })

            mov_type = mov_types[mov_code]

            observation = (
                'Cadastro'
                if mov_code == 'ENTRADA'
                else original_data.get('observation', '')
            )

            movs_to_create.append(
                Movimentations(
                    item=stock,
                    movimentation=mov_type,
                    local=stock.local,  #  FK correta
                    observation=observation,
                    user=user
                )
            )

        if movs_to_create:
            Movimentations.objects.bulk_create(movs_to_create)

        # 4) Atualizar Invoice_item.is_registred para os itens afetados
        affected_item_ids = {d['item'].id for d in validated_data_list}

        for item_id in affected_item_ids:
            inv_item = Invoice_item.objects.select_for_update().get(pk=item_id)
            total_required = int(inv_item.quantity or 0)
            total_after = Stock.objects.filter(item_id=item_id).count()
            is_done = (total_after >= total_required)
            if inv_item.is_registred != is_done:
                inv_item.is_registred = is_done
                inv_item.save(update_fields=['is_registred'])

        invoice_ids = set(Invoice_item.objects.filter(id__in=affected_item_ids).values_list('invoice_number_id', flat=True)
        )
        for invoice_id in invoice_ids:
            has_unregistered_items = Invoice_item.objects.filter(
                invoice_number_id=invoice_id,
                is_registred=False
            ).exists()

            if not has_unregistered_items:
                Invoice.objects.filter(id=invoice_id).update(
                    is_complete=True
                )

        return created_stocks


class StockSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.catalog_item.name_item', read_only=True)
    item_image = serializers.URLField(source='item.catalog_item.img_url', read_only=True)

    observation = serializers.CharField(
        write_only = True,
        required=False,
        allow_blank=True
    )

    class Meta:
        model = Stock
        fields = [
            'id',
            'item',           # FK: Invoice_item
            'category',       # FK: Item_category
            'status',         # FK: Status_item
            'item_type',      # FK: Equipament_type
            'local',          # FK: Locals
            'serial_number',
            'property_number',
            'request_unit',
            'pay_unit',
            'warranty',
            'item_name',
            'item_image',
            'observation'
        ]
        list_serializer_class = StockListSerializer

    @transaction.atomic
    def create(self, validated_data):
        stock = Stock.objects.create(**validated_data)

        status_obj = validated_data.get('status')
        if not status_obj:
            raise serializers.ValidationError({'status': ['Campo obrigatório.']})

        mov_code = STATUS_TO_MOV_CODE.get(status_obj.code)
        

        if not mov_code:
            raise serializers.ValidationError({
                'status': [f'Status {status_obj.code} não possui movimentação associada.']
            })
        mov_type = Movimentation_type.objects.get(code=mov_code)

        observation = (
            'Cadastro'
            if mov_code == 'ENTRADA'
            else validated_data.get('observation')
        )


        Movimentations.objects.create(
            item=stock,
            movimentation=mov_type,
            local=stock.local,
            observation=observation,
            user=self.context['request'].user
        )

        # Atualizar is_registred do Invoice_item após criação unitária
        inv_item = stock.item
        total_required = int(inv_item.quantity or 0)
        total_after = Stock.objects.filter(item_id=inv_item.id).count()
        is_done = (total_after >= total_required)
        if inv_item.is_registred != is_done:
            inv_item.is_registred = is_done
            inv_item.save(update_fields=['is_registred'])

        return stock

    @transaction.atomic
    def update(self, instance, validated_data):
     
        new_status = validated_data.get('status')

        if new_status and new_status != instance.status:
            mov_code = STATUS_TO_MOV_CODE.get(new_status.code)

            if not mov_code:
                raise serializers.ValidationError({
                    'status': [f'Status {new_status.code} não possui movimentação associada.']
                })

            mov_type = Movimentation_type.objects.get(code=mov_code)

            Movimentations.objects.create(
                item=instance,
                movimentation=mov_type,
                local=validated_data.get('local', instance.local),
                observation=validated_data.get('observation'),
                user=self.context['request'].user
            )

        return super().update(instance, validated_data)


#Serializer para leitura no front end
class StockReadSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    item = serializers.CharField()
    item_image = serializers.URLField(source='item.catalog_item.image.url', read_only=True)
    category = serializers.CharField()
    status = serializers.CharField()
    item_type = serializers.CharField()
    local = serializers.CharField()
    serial_number = serializers.CharField()
    property_number = serializers.CharField()
    request_unit = serializers.CharField()
    pay_unit = serializers.CharField()
    warranty = serializers.DateField(format="%d/%m/%y")
    