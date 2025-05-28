from django.db import models
from contract.models import Proposal
# Create your models here.

class Invoice_type(models.Model):
    name_type = models.CharField(
        unique=True,
        max_length=20,
        verbose_name='Tipo da nota',

    )

class Invoice_item_status(models.Model):
    name_status = models.CharField(
        unique=True,
        verbose_name='Status'
    )


class Invoice(models.Model):
    proposal = models.ForeignKey(
        Proposal,
        on_delete=models.PROTECT,
        unique=True,
        related_name='number_proposal',
        verbose_name='Proposta'
    )
    invoice_type = models.ForeignKey(
        Invoice_type, 
        related_name='name_type',
        verbose_name='Tipo da nota'
    )
    invoice_item_state = models.ForeignKey(
        Invoice_item_status,
        related_name='name_status',
        verbose_name='Status do item',
    )
    invoice_number = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Numero da nota'
    )
    description = models.TextField(
        verbose_name='Descrição'
    )
    price = models.FloatField(
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


class Invoice_item(models.Model):
    invoice_number = models.ForeignKey(
        Invoice,
        related_name='invoice_number',
        verbose_name='Numero da nota',

    )
    
