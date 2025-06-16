from django.shortcuts import render

# Create your views here

from rest_framework import viewsets
from invoice.models import Invoice, Invoice_item, Invoice_type
from invoice.serializers import InvoiceSerializer, InvoiceTypeSerializer, InvoiceItemSerializer





class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class Invoice_ItemViewSet(viewsets.ModelViewSet):
    queryset = Invoice_item.objects.all()
    serializer_class = InvoiceItemSerializer


class Invoice_typeViewSet(viewsets.ModelViewSet):
    queryset = Invoice_type.objects.all()
    serializer_class = InvoiceTypeSerializer



