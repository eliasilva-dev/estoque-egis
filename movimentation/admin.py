from django.contrib import admin
from movimentation.models import Movimentation_type, Movimentations
# Register your models here.

@admin.register(Movimentation_type)
class Movimentation_type(admin.ModelAdmin):
    list_display = ['code']


@admin.register(Movimentations)
class Movimentations(admin.ModelAdmin):
    list_display = ['item', 'movimentation', 'previous_status', 'new_status','date','local','observation', 'user']
    search_fields = ['stock__serial_number']
    list_filter =  ['date', 'movimentation']
