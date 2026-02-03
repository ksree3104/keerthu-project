from django.apps import AppConfig


class ProConfig(AppConfig):
    name = 'pro'

    def ready(self):
        import pro.signals

