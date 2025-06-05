from django.apps import AppConfig


class MovimentationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movimentation'
    verbose_name='Movimentação'

    
    def ready(self):
        import movimentation.signals       
