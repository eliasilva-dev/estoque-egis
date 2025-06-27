
from rest_framework import serializers
from invoice.models import Invoice, Invoice_item, Invoice_type, Item_catalog



class InvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = '__all__'



class ItemCatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item_catalog
        fields = ['name_item', 'img_url']



class InvoiceItemSerializer(serializers.ModelSerializer):

    name_item =ItemCatalogSerializer(read_only=True)
    
    
    class Meta:
        model = Invoice_item
        fields = ['name_item', 'invoice_number', 'quantity', 'unit_cost', 'is_registred']




class InvoiceTypeSerializer(serializers.ModelSerializer):


    
    class Meta:
        model = Invoice_type
        fields = '__all__'



