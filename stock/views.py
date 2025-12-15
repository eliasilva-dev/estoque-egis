from django.shortcuts import render
from django.db import transaction

# Create your views here.
from rest_framework import viewsets
from stock.models import Stock, Item_category, Status_item, Locals, Equipament_type

from stock.serializers import StockSerializer, ItemCategorySerializer, StatusItemSerializer, LocalSerializer, EquipamamentTypeSerializer


class StockViewSet(viewsets.ModelViewSet):
    
    queryset = Stock.objects.select_related(
        'item',
        'category',
        'status',
        'item_type',
        'local'
    )
    serializer_class = StockSerializer   



    @transaction.atomic
    def create(self, request, *args, **kwargs):
        is_list = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_list)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = Item_category.objects.all()
    serializer_class = ItemCategorySerializer
    

class StatusItemViewSet(viewsets.ModelViewSet):
    queryset = Status_item.objects.all()
    serializer_class = StatusItemSerializer


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Locals.objects.all()
    serializer_class = LocalSerializer



class EquipamentTypeViewSet(viewsets.ModelViewSet):
    queryset = Equipament_type.objects.all()
    serializer_class = EquipamamentTypeSerializer



