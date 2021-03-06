from asgiref.sync import sync_to_async

from exchange_pairs.utils import GetTokens as gt

all_compared_tokens = []


@sync_to_async
def set_all_compared_tokens():
    global all_compared_tokens
    all_compared_tokens = gt(module='all', _all=True).tokens()
