from bs4 import BeautifulSoup
from asgiref.sync import sync_to_async
import requests as req

# Create your tests here.
from exchange_comparison.utils import _query


@sync_to_async
def hitbtc_token_status():
    url = 'https://hitbtc.com/system-monitor'
    resp = req.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    elems = soup.find_all('tr', class_='table__row')
    for i, elem in enumerate(elems):
        tds = elem.find_all('td')
        try:
            if len(tds) > 1:
                # print('/******************')
                # print(round(number=(i / len(elems) * 100), ndigits=2), '%', sep=' ', end='', flush=True)
                token = tds[0].text.strip()
                deposit = tds[1].text.strip()
                transfers = tds[4].text.strip()
                trading = tds[5].text.strip()
                windrawals = tds[6].text.strip()
                # print('token:', token, 'deposit:', deposit, 'transfers:', transfers, 'trading:', trading, 'windrawals:',
                #       windrawals)
                if deposit == 'Online' and transfers == 'Online' and trading == 'Online' and windrawals == 'Online':
                    _query(f"""UPDATE module_hitbtc SET is_active = 't' WHERE symbol = '{token}ETH'
                            or symbol = '{token}BTC' or symbol = '{token}USD' or symbol = 'ETH{token}'
                            or symbol = 'BTC{token}' or symbol = 'USD{token}'""")
                else:
                    _query(f"""UPDATE module_hitbtc SET is_active = 'f' WHERE symbol = '{token}ETH'
                            or symbol = '{token}BTC' or symbol = '{token}USD' or symbol = 'ETH{token}'
                            or symbol = 'BTC{token}' or symbol = 'USD{token}'""")
                # print('******************/')
        except:
            pass


if __name__ == '__main__':
    hitbtc_token_status()
