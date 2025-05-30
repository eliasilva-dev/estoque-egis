from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Contract(models.Model):
    number_contract = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Número do contrato',
    )
    contract_name = models.CharField(
        max_length=50,
        verbose_name='Nome do contrato'
    )
    start_date = models.DateField(
        verbose_name='Data de Inicio'

    )
    end_date = models.DateField(
        verbose_name='Data de Termino'
    )

    is_active = models.BooleanField(
         default=True,
         verbose_name='Ativo'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    def clean(self):
         if self.start_date > self.end_date:
              raise ValidationError('A data de inicio não pode ser após a data de término')
         
    def __str__(self):
         return self.contract_name



class Proposal(models.Model):
      contract = models.ForeignKey(
           Contract, 
           on_delete=models.PROTECT,
           related_name='contratcs',
           verbose_name='Numero do contrato'
      )
      number_proposal = models.CharField(
           max_length=30,
           unique=True,
           verbose_name='Numero da proposta'
      )
      
      description = models.TextField(
           verbose_name='Descrição'
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
           return self.number_proposal