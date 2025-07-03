from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from stock.models import Stock, Item_category, Status_item
from stock.serializers import StockSerializer, ItemCategorySerializer, StatusItemSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.select_related(
        'invoice_number__name_item',
        'category',
        'status',
        'item_type',
        'local'
    )
    serializer_class = StockSerializer   


class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = Item_category.objects.all()
    serializer_class = ItemCategorySerializer
    

class StatusItemViewSet(viewsets.ModelViewSet):
    queryset = Status_item.objects.all()
    serializer_class = StatusItemSerializer
