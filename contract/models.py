from django.db import models

# Create your models here.
class Contract(models.Model):
    number_contract = models.IntegerField(
        unique=True,
        verbose_name='Numero do Contrato',
    )
    name_contract = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Nome do Contrato'
    )
    start_date = models.DateField(
        verbose_name='Data de Inicio'

    )

    end_date = models.DateField(
        verbose_name='Data de Termino'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )



class Proposal(models.Model):
      contract = models.ForeignKey(
           Contract, 
           on_delete=models.PROTECT,
           related_name='name_contract',
           verbose_name='Nome do contrato'
      )
      number_proposal = models.IntegerField(
           unique=True,
           verbose_name='Numero da proposta'
      )
      
      description = models.TextField(
           verbose_name='Descrição'
      )
      is_active = models.BooleanField(
           verbose_name='Ativo'
      )
      created_at = models.DateTimeField(
           auto_now_add=True,
           verbose_name='Criado em'
      )
      updated_at = models.DateTimeField(
           auto_now=True,
           verbose_name='Atualizaddo em'
      )