from django.db import models
from contract.models import Proposal
# Create your models here.

class Invoice_type(models.Model):
    name_type = models.CharField(
        unique=True,
        max_length=20,
        verbose_name='Tipo da nota',
    )
    def __str__(self):
        return str(self.name_type)

class Invoice_item_status(models.Model):
    name_status = models.CharField(
        unique=True,
        verbose_name='Status'
    )
    def __str__(self):
        return str(self.name_status)



class Item_catalog(models.Model):
    name_item = models.CharField(
        max_length=25,
        unique=True,
        verbose_name='Nome do Item'
    )
    img_url = models.URLField(
        verbose_name='Link da Imagem',
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.name_item

class Invoice(models.Model):
    proposal = models.ForeignKey(
        Proposal,
        on_delete=models.PROTECT,
        related_name='proposals',
        verbose_name='Numero da Proposta'
    )
    invoice_type = models.ForeignKey(
        Invoice_type, 
        on_delete=models.PROTECT,
        related_name='type',
        verbose_name='Tipo da nota'
    )
    invoice_number = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Numero da nota'
    )
    description = models.TextField(
        verbose_name='Descrição'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Valor'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizaddo em'
    )
    def __str__(self):
        return self.invoice_number


class Invoice_item(models.Model):
    invoice_number = models.ForeignKey(
        Invoice,
        on_delete=models.PROTECT,
        related_name='invoices',
        verbose_name='Numero da nota',

    )
    name_item = models.ForeignKey(
        Item_catalog,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name='Nome do item',
    )
    status_item = models.ForeignKey(
        Invoice_item_status,
        on_delete=models.PROTECT,
        related_name='status',
        verbose_name='Status do item',

    )
    unit_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Custo unitário',
    )
    quantity = models.IntegerField(
        verbose_name='Quantidade',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizaddo em'
    )


    def __str__(self):
        return self.invoice_number


    

