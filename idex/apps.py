from django.apps import AppConfig
from .getter import *


class IdexConfig(AppConfig):
    name = 'idex_module'

    def ready(self):
        refresh()
        pass
