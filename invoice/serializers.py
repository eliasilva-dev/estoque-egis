
from rest_framework import serializers
from invoice.models import Invoice, Invoice_item, Invoice_type



class InvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice_item
        fields = '__all__'



class InvoiceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice_type
        fieldes = '__all__'