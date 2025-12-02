from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from invoice.models import Invoice, Invoice_item, Invoice_type, Item_catalog
from invoice.serializers import InvoiceSerializer, InvoiceReadSerializer,InvoiceTypeSerializer, InvoiceItemSerializer, ItemCatalogSerializer, NotRegisteredInvoices, InvoiceItemReadOnlySerializer





class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


    def create(self, request, *args, **kwargs):
        #get serializer on request
        serializer = self.get_serializer(data=request.data)
        #verify if the serializer is valid
        serializer.is_valid(raise_exception=True)
        #save the obj of serializer 
        invoice = serializer.save()

        #response to tranform serializer
        response_serializer = InvoiceReadSerializer(invoice)
        
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        invoice = serializer.save()

        response_serializer = InvoiceReadSerializer(invoice)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
       


class InvoiceListReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceReadSerializer

class NotRegisterInvoicesView(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.filter(is_complete=False)
    serializer_class = NotRegisteredInvoices


class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = Invoice_item.objects.all()
    serializer_class = InvoiceItemSerializer

class InvoiceItemReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice_item.objects.all()
    serializer_class = InvoiceItemReadOnlySerializer


class InvoicetypeViewSet(viewsets.ModelViewSet):
    queryset = Invoice_type.objects.all()
    serializer_class = InvoiceTypeSerializer



class ItemCatalogViewSet(viewsets.ModelViewSet):
    queryset = Item_catalog.objects.all()
    serializer_class = ItemCatalogSerializer