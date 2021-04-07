from pathlib import Path

from asgiref.sync import sync_to_async
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create your tests here.
from exchange_comparison.utils import _query

options = Options()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("--window-size=1366,768")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# DRIVER_FILE = str(Path(__file__).resolve(strict=True).parent) + '/chromedriver'
DRIVER_FILE = str(Path(__file__).resolve(strict=True).parent) + '/win_chromedriver.exe'
# sys.path.append(DRIVER_FILE)
driver = webdriver.Chrome(executable_path=DRIVER_FILE, chrome_options=options)


class ModelReferences(object):
    def init(self, driver, urls):
        self.driver = driver
        self.urls = urls

    def get_html(self):
        self.driver.get(self.urls)
        return self.driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div/table/tbody/tr')


@sync_to_async
def hitbtc_token_status():
    url = 'https://hitbtc.com/system-monitor'
    driver.get(url)
    elems = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div/table/tbody/tr')
    for i, elem in enumerate(elems):
        try:
            if elem.find_element_by_xpath('td[2]'):
                # print('/******************')
                # print(round(number=(i / len(elems) * 100), ndigits=2), '%', sep=' ', end='', flush=True)
                token = elem.find_element_by_xpath('td[1]').text
                deposit = elem.find_element_by_xpath('td[2]').text
                transfers = elem.find_element_by_xpath('td[5]').text
                trading = elem.find_element_by_xpath('td[6]').text
                windrawals = elem.find_element_by_xpath('td[7]').text
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
