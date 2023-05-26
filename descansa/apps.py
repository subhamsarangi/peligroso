from django.apps import AppConfig


class DescansaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'descansa'

    def ready(self):
        import descansa.signals
