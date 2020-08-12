from django.apps import AppConfig
from .getter import *


class IdexConfig(AppConfig):
    name = 'idex'

    def ready(self):
        refresh()
        pass
