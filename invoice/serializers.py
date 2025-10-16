
from rest_framework import serializers
from invoice.models import Invoice, Invoice_item, Invoice_type, Item_catalog



class InvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = ['proposal','invoice_number', 'description', 'invoice_type', 'price', 'is_complete']



class InvoiceReadSerializer(serializers.Serializer):
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
        fields = ['name_item', 'img_url']



class InvoiceItemSerializer(serializers.ModelSerializer):

    catalog_item = ItemCatalogSerializer(read_only=True)
    invoice_number = serializers.CharField(source="invoice_number.invoice_number")
    
    
    class Meta:
        model = Invoice_item
        fields = ['catalog_item', 'invoice_number', 'quantity', 'unit_cost', 'is_registred']




class InvoiceTypeSerializer(serializers.ModelSerializer):


    
    class Meta:
        model = Invoice_type
        fields = '__all__'



