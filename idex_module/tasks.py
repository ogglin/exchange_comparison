import sys

from exchange_comparison._celery import app
from .services import set_currencies


# @app.task
# def currencies_update():
#     print('collect Idex update')
#     set_currencies()


@app.task
def currencies_beat_update():
    try:
        print('try collect Idex update')
        set_currencies()
        print('Idex data collected')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
