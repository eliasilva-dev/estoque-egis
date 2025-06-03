from django.db import models
from stock.models import Stock
from user.models import User
# Create your models here.
class Movimentation_type(models.Model):
    movimentation_name = models.CharField(max_length=15, unique=True)



    class Meta: 
        verbose_name='Movimentação'
        verbose_name_plural = 'Tipos de movimentação'

    def __str__(self):
        return str(self.movimentation_name)


class Movimentations(models.Model):
    item = models.ForeignKey(
        Stock,
        on_delete=models.PROTECT,
        related_name='stock',
        verbose_name='Número de série',

    )



    movimentation = models.ForeignKey(
        Movimentation_type,
        on_delete=models.PROTECT,
        related_name='movimentation',
        verbose_name='Tipo de movimentação',

    )

    date = models.DateField(verbose_name='Data', auto_now_add=True)
    observation = models.TextField(
        null=True,
        blank=True,
        verbose_name='Obeservação'
    )

    user = models.ForeignKey(
        User,
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

