import datetime

from django.core.management.base import BaseCommand

from exchange_pairs.main import init_start, init_start_test

# from exchange_pairs.tests import set_new_token
# from exchange_comparison.test_utils import init_test


class Command(BaseCommand):
    help = 'Compare exchange markets'

    def handle(self, *args, **options):
        # if options['set_new_token']:
        #     set_new_token()
        if options['start_all']:
            print('Start all exchange')
            init_start()
        if options['test']:
            print('Start test', datetime.datetime.now())
            # init_test()
            print('End test', datetime.datetime.now())
        if options['hbtc']:
            print('Start Hitbtc', datetime.datetime.now())
            init_start_test()
            print('End Hitbtc', datetime.datetime.now())

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
        parser.add_argument(
            '-test',
            '--test',
            action='store_true',
            default=False,
            help='Start test'
        )
        parser.add_argument(
            '-hbtc',
            '--hbtc',
            action='store_true',
            default=False,
            help='Hitbtc test'
        )
