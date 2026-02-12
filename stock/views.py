from django.shortcuts import render
from django.utils import timezone
from django.db import transaction
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
from django.db.models import Sum, Count
from rest_framework import viewsets
from stock.models import Stock, Item_category, Status_item, Locals, Equipament_type

from stock.serializers import StockSerializer, ItemCategorySerializer, StatusItemSerializer, LocalSerializer, EquipamamentTypeSerializer, StockReadSerializer


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



class StockReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockReadSerializer




class StockStateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        today = timezone.now().date()

        total_in_stock = Stock.objects.filter(status__status_name="Em estoque").count()
        total_active = Stock.objects.filter(status__status_name="Ativo").count()

        warranty_items = Stock.objects.filter(
            warranty=today
        ).count()


        data = {
            "total_stock" : total_in_stock,
            "total_active": total_active,
            "total_in_warranty": warranty_items
        }


        return Response(data)
