from rest_framework import serializers
from stock.models import Stock, Item_category, Status_item, Locals, Equipament_type
from movimentation.models import Movimentations, Movimentation_type
from invoice.serializers import ItemCatalogSerializer

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





class StockSerializer(serializers.ModelSerializer):
    
   
    item_name = serializers.CharField(source='item.name_item.name_item', read_only=True)
    item_image = serializers.URLField(source='item.name_item.img_url', read_only=True)
    category = ItemCategorySerializer()
    item_type = EquipamamentTypeSerializer()
    status = StatusItemSerializer()
    local = LocalSerializer()


    def create(self, validated_data): 
        stock = Stock.objects.create(**validated_data)
        print("Obejto Criado")
        try:
            if validated_data['status'].status_name == "Em estoque":
                print("Dentro do do if")
                movimentation_type = Movimentation_type.objects.get(movimentation_name='Entrada')
                print("User: ",self.context['request'].user)
                mov = Movimentations.objects.create(
                    item = stock,
                    movimentation = movimentation_type,
                    local = stock.local.local_name,
                    observation = 'Cadastro',
                    user = self.context['request'].user
                )
                print(f"Criado a movimentacao {movimentation_type}")
                mov.save()
        except Exception as e:
            print("Erro ao criar movimentação", e)

        return stock
    
    def update(self, instance, validated_data):
        #acess to current status of item 
        old_status = instance.status
        
        #Verify on the request body if status is present
        print('Current State:', old_status)
        if 'status' in validated_data:
            print('Into first if status is in validated_data')
            #get the new status recived by request body 
            new_status = validated_data.get('status')
            print('New Status:', new_status)
            #verify if the status was changed
            if new_status != old_status:
                print(f'Into if where {new_status} != {old_status}')
                if new_status.status_name == "Em estoque":
                    #if the new_status is 'Em estoque' the item has returned to stock, so the movimentation should be 'Entrada'
                    movimentation_type = Movimentation_type.objects.get(movimentation_name='Entrada')
                    mov = Movimentations.objects.create(
                        item = instance,
                        movimentation = movimentation_type,
                        local = instance.local.local_name,
                        user = self.context['request'].user

                    )
                    print('movimentation Entrada registred')
                #if not, the item could be (Ativo(em uso), (Removido), (Manuntencao) (tranferencia) ) in this cases the movimentation should be 'Saida' beacause the itens is not avalaible on stock 
                else:
                    print('Registering other cases')
                    movimentation_type = Movimentation_type.objects.get(movimentation_name='Saida')
                    mov = Movimentations.objects.create(
                        item = instance,
                        movimentation=movimentation_type,
                        local = instance.local.local_name,
                        user = self.context['request'].user
                    )
                mov.save()
        return super().update(instance, validated_data)

    
    class Meta:
        model = Stock
        fields = [
            'id',
            'item_name',
            'serial_number',
            'property_number',
            'item_image',
            'category',
            'status',
            'item_type',
            'local',
            'request_unit',
            'pay_unit',
            'warranty',
        ]

