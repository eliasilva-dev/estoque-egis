from rest_framework import serializers
from stock.models import Stock, Item_category



class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stock
        fields = '__all__'


class ItemCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item_category
        fields = '__all__'