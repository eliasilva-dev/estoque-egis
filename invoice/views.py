from django.shortcuts import render

# Create your views here

from rest_framework import viewsets
from invoice.models import Invoice, Invoice_item, Invoice_type, Item_catalog
from invoice.serializers import InvoiceSerializer, InvoiceReadSerializer,InvoiceTypeSerializer, InvoiceItemSerializer, ItemCatalogSerializer, NotRegisteredInvoices





class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceListReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceReadSerializer

class NotRegisterInvoicesView(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.filter(is_complete=False)
    serializer_class = NotRegisteredInvoices


class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = Invoice_item.objects.all()
    serializer_class = InvoiceItemSerializer


class InvoicetypeViewSet(viewsets.ModelViewSet):
    queryset = Invoice_type.objects.all()
    serializer_class = InvoiceTypeSerializer



class ItemCatalogViewSet(viewsets.ModelViewSet):
    queryset = Item_catalog.objects.all()
    serializer_class = ItemCatalogSerializer