from django.db import models
from contract.models import Proposal
# Create your models here.

class Invoice_type(models.Model):
    name_type = models.CharField(
        unique=True,
        max_length=20,
        verbose_name='Tipo da nota',
    )
    
    class Meta: 
        verbose_name_plural = 'Tipo da nota'

    def __str__(self):
        return str(self.name_type)

   


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

    class Meta: 
        verbose_name_plural = 'Catalogo de Itens'
    
    def __str__(self):
        return str(self.name_item)



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


    class Meta: 
        verbose_name_plural = 'Notas Fiscais'
    

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
        related_name='itens',
        verbose_name='Nome do item',
    )

    is_registred = models.BooleanField(
        default=False,
        verbose_name='Cadastrado',
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

    class Meta: 
        verbose_name_plural = 'Itens da nota'


    def __str__(self):
        return str(self.invoice_number)


    

