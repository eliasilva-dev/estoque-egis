from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.PROTECT,
        related_name='user',
        blank=True,
        null=True,
        verbose_name='Usuário',
    )
    phone_number = models.CharField(
        blank=True,
        null=True,
        max_length=15
    )

    department = models.CharField(
        max_length=20,
        blank=True,
        null=True

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
        return str(self.user.username)