from django.shortcuts import render
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status

# Create your views here.
from rest_framework import viewsets
from stock.models import Stock, Item_category, Status_item, Locals, Equipament_type

from stock.serializers import StockSerializer, ItemCategorySerializer, StatusItemSerializer, LocalSerializer, EquipamamentTypeSerializer


class StockViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    
    queryset = Stock.objects.all()
    serializer_class = StockSerializer   



    @transaction.atomic
    def create(self, request, *args, **kwargs):
        is_list = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_list)
        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=400)
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



