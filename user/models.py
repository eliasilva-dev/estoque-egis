from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.PROTECT,
        related_name='user',
        blank=True,
        null=True,
        verbose_name='Usuário',
    )
    email = models.CharField(
        max_length=100,
        verbose_name='E-mail',
        unique=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Ataualizado em'

    )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural ='Usuários'

    def __str__(self):
        return str(self.email)