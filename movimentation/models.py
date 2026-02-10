from django.db import models
from django.conf import settings
from stock.models import Stock, Locals, Status_item
from user.models import User
# Create your models here.


class Movimentation_type(models.Model):
    code = models.CharField(max_length=20,  verbose_name='Código', default='')

    description = models.CharField(max_length=50, verbose_name='Descrição', default='')

    class Meta: 
        verbose_name='Tipo de Movimentação'
        verbose_name_plural = 'Tipos de movimentação'

    def __str__(self):
        return str(self.description)


class Movimentations(models.Model):

    MOVIMENT_FLOW = (
        ('IN', 'Entrada'),
        ('OUT', 'Saída')
    )


    item = models.ForeignKey(
        Stock,
        on_delete=models.PROTECT,
        related_name='movimentations',
        verbose_name='Número de série',

    )



    movimentation = models.ForeignKey(
        Movimentation_type,
        on_delete=models.PROTECT,
        related_name='movimentations',
        verbose_name='Tipo de movimentação',

    )

    moviment_flow = models.CharField(max_length=3,
                                     choices=MOVIMENT_FLOW, verbose_name='Fluxo de movimentação')
    
    previous_status = models.ForeignKey(
        Status_item,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Status anterior',
        related_name='+'
        
    )
    new_status = models.ForeignKey(Status_item, on_delete=models.PROTECT,related_name='+', verbose_name='Novo status', blank=True, null=True)
    date = models.DateField(verbose_name='Data', auto_now_add=True)

    local = models.ForeignKey(
        Locals,
        on_delete=models.PROTECT,

        
        verbose_name='Localidade'
    )
    observation = models.TextField(
        null=True,
        blank=True,
        verbose_name='Obeservação'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Usuário',

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
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'

