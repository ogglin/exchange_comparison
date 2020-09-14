import requests
import json
from .models import *


def currencies_update(direction, lowest_ask, highest_bid):
    pair_id = Idex.objects.filter(exch_direction=direction).values('id')
    if len(pair_id) > 0:
        Idex.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid)
    else:
        pair = Idex(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True)
        pair.save()


def set_currencies():
    lowest_ask = 0
    highest_bid = 0
    url = 'https://api.idex.market/returnTicker'
    response = requests.get(url=url)
    jData = json.loads(response.content)
    for key in jData.keys():
        exch_direction = key
        for item in jData[key].items():
            if str(item[0]) == 'lowestAsk':
                if item[1] != 'N/A':
                    lowest_ask = item[1]
                else:
                    lowest_ask = 0
            if str(item[0]) == 'highestBid':
                if item[1] != 'N/A':
                    highest_bid = item[1]
                else:
                    lowest_ask = 0
        currencies_update(exch_direction, lowest_ask, highest_bid)



'''
wss://datastream.idex.market
{
  "request": "handshake",
  "payload": "{\"version\": \"1.0.0\", \"key\": \"api:rbXUPt_TeOMzWRBpd8O_d\"}"
}

{
"action": "subscribe",
"topics": ["ETH_AURA", "ETH_IDXM"],
"events": ["market_orders", "market_cancels", "market_trades"]
}


{
    "sid": "sid:tmuTRa_Zx_4s",
    "request": "subscribeToMarkets",
    "payload": "{\"topics\": [\"ETH_AURA\", \"ETH_IDXM\"], \"events\": [\"market_orders\", \"market_cancels\", \"market_trades\"] }"
}

{
	"sid": "sid:62hgXpkqmMIv",
	"request": "subscribeToMarkets",
	"payload": "{\"topics": [\"ETH_AURA\", \"ETH_IDXM\"], \"events": [\"market_orders\", \"market_cancels\", \"market_trades\"] }"
}

{
	"sid": "sid:hMeIjxvKbZQM",
	"request": "subscribeToMarkets",
	"payload": "{\"topics\": [\"ETH_AURA\", \"ETH_IDXM\"], \"events\": [\"market_trades\"] }"
}
{"sid": "sid:mvrtfwiT-S1","request": "subscribeToMarkets","payload": "{\"topics\": [\"ETH_AURA\", \"ETH_IDXM\"], \"events": [\"market_orders\", \"market_cancels\", \"market_trades\"] }"}

{
    "sid": "62hgXpkqmMIv",
    "request": "subscribeToMarkets",
    "payload": "{\"action\": \"unsubscribe\", \"topics\": [\"ETH_AURA\", \"ETH_IDXM\"] }"
  }

'''