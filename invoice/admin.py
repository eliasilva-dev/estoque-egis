from django.contrib import admin

# Register your models here.
from invoice.models import Invoice, Invoice_item, Invoice_item_status, Invoice_type, Item_catalog
from movimentation.models import Movimentation_type, Movimentations
from stock.models import Item_category, Status_item, Equipament_type, Locals, Stock


@admin.register(Invoice_type)
class Invoice_type(admin.ModelAdmin):
    list_display = ['name_type']


@admin.register(Item_catalog)
class Item_catalog(admin.ModelAdmin):
    list_display = ['name_item']
    

@admin.register(Invoice_item_status)
class Invoice_item_status(admin.ModelAdmin):
    list_display = ['name_status']

@admin.register(Invoice)
class Invoice(admin.ModelAdmin):
    list_display =  ['proposal', 'invoice_type', 'invoice_number', 'description', 'price']
    search_fields = ['invoice_number', 'proposal__number_proposal']
    list_filter = ['price', 'invoice_type']

@admin.register(Invoice_item)
class Invoice_item(admin.ModelAdmin):
    list_display = ['invoice_number', 'name_item', 'status_item', 'unit_cost', 'quantity']
    search_fields = ['name_item', 'invoice_number']
    list_filter = ['status_item']



@admin.register(Movimentation_type)
class Movimentation_type(admin.ModelAdmin):
    list_display = ['movimentation_name']


@admin.register(Movimentations)
class Movimentations(admin.ModelAdmin):
    list_display = ['item', 'movimentation', 'date', 'observation', 'user']
    search_fields = ['stock__serial_number']
    list_filter =  ['date']


@admin.register(Item_category)
class Item_category(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(Status_item)
class Status_item(admin.ModelAdmin):
    list_display = ['status_name']


@admin.register(Equipament_type)
class Equipament_type(admin.ModelAdmin):
    list_display = ['equipament_type']

@admin.register(Locals)
class Locals(admin.ModelAdmin):
    list_display = ['local_name']

@admin.register(Stock)
class Stock(admin.ModelAdmin):
    list_display = ['invoice_number', 'category', 'status', 'item_type', 'local', 'serail_number', 'property_number', 'request_unit', 'pay_unit', 'warranty']

