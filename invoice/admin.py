from django.contrib import admin

# Register your models here.
from invoice.models import Invoice, Invoice_item, Invoice_type, Item_catalog
from contract.models import Proposal




@admin.register(Invoice_type)
class Invoice_type(admin.ModelAdmin):
    list_display = ['name_type']


@admin.register(Item_catalog)
class Item_catalog(admin.ModelAdmin):
    list_display = ['name_item']
    



@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display =  ['id', 'proposal', 'invoice_type', 'invoice_number', 'description', 'price', 'is_complete']
    search_fields = ['invoice_number','proposal__number_proposal']
    list_filter = ['price', 'invoice_type']


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "proposal":
            kwargs["queryset"] = Proposal.objects.filter(is_registred=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



@admin.register(Invoice_item)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_number', 'catalog_item', 'unit_cost', 'quantity', 'is_registred']
    search_fields = ['invoice_number__invoice_number', 'catalog_item__name_item']
    list_filter = ['is_registred']


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "invoice_number":
            kwargs["queryset"] = Invoice.objects.filter(is_complete=False) 
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)






