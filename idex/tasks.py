from exchange_comparison._celery import app
from .models import Idex


@app.task
def pair_exch_add(direction, lowest_ask, highest_bid):
    pair = Idex(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid)
    pair.save()
    return pair


@app.task
def pair_exch_update(direction, lowest_ask, highest_bid):
    pair_id = Idex.objects.filter(exch_direction=direction).values('id')
    pair = Idex(id=pair_id, exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid)
    pair.save()
    return pair
