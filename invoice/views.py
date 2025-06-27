from django.shortcuts import render

# Create your views here

from rest_framework import viewsets
from invoice.models import Invoice, Invoice_item, Invoice_type, Item_catalog
from invoice.serializers import InvoiceSerializer, InvoiceTypeSerializer, InvoiceItemSerializer, ItemCatalogSerializer





class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = Invoice_item.objects.select_related('name_item')
    serializer_class = InvoiceItemSerializer


class InvoicetypeViewSet(viewsets.ModelViewSet):
    queryset = Invoice_type.objects.all()
    serializer_class = InvoiceTypeSerializer



class ItemCatalogViewSet(viewsets.ModelViewSet):
    queryset = Item_catalog.objects.all()
    serializer_class = ItemCatalogSerializer