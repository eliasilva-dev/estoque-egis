from django.contrib import admin

# Register your models here.
from contract.models import Contract, Proposal


@admin.register(Contract)
class Contract(admin.ModelAdmin):
    list_display= ['number_contract', 'contract_name', 'start_date', 'end_date', 'is_active','was_delete']
    search_fields = ['number_contract', 'contract_name']
    list_filter = ['start_date', 'is_active', 'was_delete']


@admin.register(Proposal)
class Proposal(admin.ModelAdmin):
    list_display=['contract', 'number_proposal', 'description', 'is_registred', 'was_delete']
    search_fields=['number_proposal']
    list_filter = ['contract']