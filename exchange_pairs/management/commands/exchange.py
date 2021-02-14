import subprocess

from django.core.management.base import BaseCommand

from bancor_module.services import bankor_init
from exchange_pairs.functions import exchanges_init
from idex_module.services import idex_init
from kyber_module.services import kyber_init
from uniswap_module.services import uniswap_v2_init, uniswap_v1_init


class Command(BaseCommand):
    help = 'Compare exchange markets'

    def handle(self, *args, **options):
        if options['exch']:
            print('Start compare exchange')
            exchp = subprocess.Popen('python /var/www/exchange_comparison/exchange_pairs/start.py &').pid
            print("done. (PID: %s)" % exchp)
        if options['idex']:
            print('Start collect idex tickers')
            idexp = subprocess.Popen(idex_init()).pid
            print("done. (PID: %s)" % idexp)
        if options['bankor']:
            print('Start collect bankor tickers')
            bankorp = subprocess.Popen(bankor_init()).pid
            print("done. (PID: %s)" % bankorp)
        if options['kyber']:
            print('Start collect kyber tickers')
            kyberp = subprocess.Popen(kyber_init())
            print("done. (PID: %s)" % kyberp)
        if options['uniswap']:
            print('Start collect uniswap tickers')
            unip = subprocess.Popen(uniswap_v2_init()).pid
            print("done. (PID: %s)" % unip)
        if options['uniswap_one']:
            print('Start collect uniswap-one tickers')
            uniop = subprocess.Popen(uniswap_v1_init()).pid
            print("done. (PID: %s)" % uniop)

    def add_arguments(self, parser):
        parser.add_argument(
            '-b',
            '--bankor',
            action='store_true',
            default=False,
            help='Start collect bankor tickers'
        )
        parser.add_argument(
            '-k',
            '--kyber',
            action='store_true',
            default=False,
            help='Start collect kyber tickers'
        )
        parser.add_argument(
            '-u',
            '--uniswap',
            action='store_true',
            default=False,
            help='Start collect uniswap tickers'
        )
        parser.add_argument(
            '-uo',
            '--uniswap_one',
            action='store_true',
            default=False,
            help='Start collect uniswap_one tickers'
        )
        parser.add_argument(
            '-i',
            '--idex',
            action='store_true',
            default=False,
            help='Start collect idex tickers'
        )
        parser.add_argument(
            '-ex',
            '--exch',
            action='store_true',
            default=False,
            help='Start compare exchange'
        )