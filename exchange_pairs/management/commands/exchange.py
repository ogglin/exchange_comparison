import subprocess

from django.core.management.base import BaseCommand

from bancor_module.services import bankor_init
from exchange_pairs.functions import exchanges_idex, exchanges_hotbit
from exchange_pairs.main import init_start
# from exchange_pairs.tests import set_new_token
from idex_module.services import idex_init
from kyber_module.services import kyber_init
from uniswap_module.services import uniswap_v2_init, uniswap_v1_init


class Command(BaseCommand):
    help = 'Compare exchange markets'

    def handle(self, *args, **options):
        # if options['set_new_token']:
        #     set_new_token()
        if options['start_all']:
            print('Start all exchange')
            startp = subprocess.Popen(init_start()).pid
            print("done. (PID: %s)" % startp)

    def add_arguments(self, parser):
        # parser.add_argument(
        #     '-snt',
        #     '--set_new_token',
        #     action='store_true',
        #     default=False,
        #     help='Start all set_new_token'
        # )
        parser.add_argument(
            '-all',
            '--start_all',
            action='store_true',
            default=False,
            help='Start all exhcanges'
        )

