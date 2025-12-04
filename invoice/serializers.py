
from rest_framework import serializers
from invoice.models import Invoice, Invoice_item, Invoice_type, Item_catalog



class InvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = ['id', 'proposal','invoice_number', 'description', 'invoice_type', 'price', 'is_complete']






class InvoiceReadSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    proposal = serializers.CharField()
    invoice_number = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    invoice_type = serializers.CharField()
    is_complete = serializers.BooleanField()


class NotRegisteredInvoices(serializers.Serializer):
     id = serializers.IntegerField()
     invoice_number = serializers.CharField()


class ItemCatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item_catalog
        fields = ['id','name_item', 'img_url']








class InvoiceItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Invoice_item
        fields = ['catalog_item', 'invoice_number', 'quantity', 'unit_cost', 'is_registred']


class InvoiceItemReadOnlySerializer(serializers.Serializer):
     
     catalog_item = serializers.CharField()
     invoice_number = serializers.CharField()
     unit_cost = serializers.CharField()
     quantity = serializers.IntegerField()
     is_registred = serializers.BooleanField()



class InvoiceTypeSerializer(serializers.ModelSerializer):


    
    class Meta:
        model = Invoice_type
        fields = '__all__'



