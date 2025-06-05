from django.contrib import admin

# Register your models here.
from invoice.models import Invoice, Invoice_item, Invoice_type, Item_catalog




@admin.register(Invoice_type)
class Invoice_type(admin.ModelAdmin):
    list_display = ['name_type']


@admin.register(Item_catalog)
class Item_catalog(admin.ModelAdmin):
    list_display = ['name_item']
    



@admin.register(Invoice)
class Invoice(admin.ModelAdmin):
    list_display =  ['proposal', 'invoice_type', 'invoice_number', 'description', 'price']
    search_fields = ['invoice_number','proposal__number_proposal']
    list_filter = ['price', 'invoice_type']



@admin.register(Invoice_item)
class Invoice_item(admin.ModelAdmin):
    list_display = ['invoice_number', 'name_item', 'unit_cost', 'quantity', 'is_registred']
    search_fields = ['invoice_number__invoice_number', 'name_item__name_item']
    list_filter = ['is_registred']




