from django.contrib import admin

# Register your models here.
from invoice.models import Invoice, Invoice_item, Invoice_item_status, Invoice_type, Item_catalog

@admin.register(Invoice_type)
class Invoice_type(admin.ModelAdmin):
    list_display = ['name_type']


@admin.register(Item_catalog)
class Item_catalog(admin.ModelAdmin):
    list_display = ['name_item']
    search_fields = ['name_item']

@admin.register(Invoice_item_status)
class Invoice_item_status(admin.ModelAdmin):
    list_display = ['name_status']

@admin.register(Invoice)
class Invoice(admin.ModelAdmin):
    list_display =  ['proposal', 'invoice_type', 'invoice_number', 'description', 'price']
    search_fields = ['invoice_number', 'proposal']
    list_filter = ['price', 'invoice_type']

@admin.register(Invoice_item)
class Invoice_item(admin.ModelAdmin):
    list_display = ['invoice_number', 'name_item', 'status_item', 'unit_cost', 'quantity']
    search_fields = ['name_item', 'invoice_number']
    list_filter = ['status_item']




