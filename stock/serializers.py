from rest_framework import serializers
from stock.models import Stock, Item_category, Status_item, Locals
from movimentation.models import Movimentations, Movimentation_type
from invoice.serializers import ItemCatalogSerializer



class StockSerializer(serializers.ModelSerializer):
    
    invoice_number = serializers.StringRelatedField(read_only=True)
    item_name = serializers.CharField(source='invoice_number.name_item.name_item', read_only=True)
    item_image = serializers.URLField(source='invoice_number.name_item.img_url', read_only=True)
    category = serializers.StringRelatedField()
    item_type = serializers.StringRelatedField()
    status = serializers.PrimaryKeyRelatedField(queryset=Status_item)
    local = serializers.PrimaryKeyRelatedField(queryset=Locals)


    def create(self, validated_data):
        
        stock = Stock.objects.create(**validated_data)
        print("Criei o obj")
        if validated_data['status'].status_name == "Em estoque":
            movimentation_type = Movimentation_type.objects.get(movimentation_name='Entrada')
            print("User: ",self.context['request'].user)
            mov = Movimentations.objects.create(
                item = stock,
                movimentation = movimentation_type,
                local = stock.local.local_name,
                observation = 'Cadastro',
                user = self.context['request'].user
            )
            mov.save()

        
        return stock

    
    class Meta:
        model = Stock
        fields = [
            'id',
            'invoice_number',
            'serial_number',
            'property_number',
            'item_name',
            'item_image',
            'category',
            'status',
            'item_type',
            'local',
            'request_unit',
            'pay_unit',
            'warranty',
            'created_at',
            'updated_at',
        ]


class ItemCategorySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Item_category
        fields = '__all__'