from exchange_pairs.utils import GetTokens as gt
from uniswap_module.functions import get_uni_2

all_compared_tokens = []
uniswap_prices_set = []


async def set_all_compared_tokens():
    global all_compared_tokens
    global uniswap_prices_set
    uniswap_prices_set = await get_uni_2()
    all_compared_tokens = gt(module='all', _all=True).tokens()
    all_compared_tokens.extend(uniswap_prices_set)
    # if len(all_compared_tokens) > 0:
    #     print('all_compared_tokens', len(all_compared_tokens))
