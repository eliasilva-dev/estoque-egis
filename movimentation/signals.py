from django.db.models.signals import post_save
from django.dispatch import receiver
from movimentation.models import Movimentation_type, Movimentations
from stock.models import Stock




'''
@receiver(post_save, sender=Stock)
def create_movimentation(sender, instance, created, **kwargs):
   if created:
      if instance.status.status_name == 'Em estoque':
        moviment_type = Movimentation_type.objects.get(movimentation_name='Entrada')
        Movimentations.objects.create(
           item = instance,
           movimentation = moviment_type,
           local = instance.local.local_name,
           user= None,
           observation='Teste preenchimento'
        )


'''  