from django.contrib import admin
from stock.models import Item_category, Status_item, Equipament_type, Locals, Stock
# Register your models here.




@admin.register(Stock)
class Stock(admin.ModelAdmin):
    list_display = ['id','item','serial_number', 'category','property_number', 'request_unit', 'pay_unit','local', 'status', 'item_type','warranty',  'updated_at']

    search_fields = ['serial_number', 'property_number']
    list_filter = ['status', 'local', 'item_type']





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


