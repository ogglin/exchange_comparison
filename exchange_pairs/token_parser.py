import json

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Create your tests here.
# from exchange_comparison.utils import _query
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

driver = webdriver.Chrome(executable_path='../chromedriver.exe', chrome_options=options)


def set_new_token():
    # url = 'https://api.hotbit.io/api/v1/asset.list'
    # url = 'https://cn.etherscan.com/tokenholdings?a=0x274f3c32c90517975e29dfc209a23f315c1e5fc7&ps=100&sort=total_price_usd&order=desc'
    url = 'https://etherscan.io/gastracker'
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    # print(driver.find_element(By.TAG_NAME, "main").text)
    print(driver.find_element(By.TAG_NAME, "body").text)
    elems = driver.find_elements_by_xpath('/html/body/div[1]/main')
    print(elems)
    # for data in jData:
    #     # print(jData[data])
    #     token = jData[data]['symbol']
    #     decimals = jData[data]['decimals']
    #     contract = jData[data]['address']
    #     # row = f"INSERT INTO trusted_pairs(token, contract, decimals, is_active, tsymbol) VALUES ('{token}', '{contract}', {decimals}, 'f', '{token}') ON CONFLICT (token) DO UPDATE SET contract = '{contract}';"
    #     # row = f"INSERT INTO trusted_pairs(token, contract, decimals, is_active, tsymbol) VALUES ('{token}', NULL, {decimals}, 'f', '{token}');"
    #     print(row)
    # resp = _query(row)
    # print(resp)


# set_new_token()


class ModelReferences(object):
    def init(self, driver, urls):
        self.driver = driver
        self.urls = urls

    def get_html(self):
        self.driver.get(self.urls)
        return self.driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div/table/tbody/tr')


def parce_token():
    url = 'https://hitbtc.com/system-monitor'
    driver.get(url)
    elems = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div/table/tbody/tr')
    # response = requests.get(url=url)
    # contents = response.content
    # soup = BeautifulSoup(contents, 'lxml')
    for i, elem in enumerate(elems):
        print(i)
        try:
            print('/******************')
            token = elem.find_element_by_xpath('td[1]').text
            deposit = elem.find_element_by_xpath('td[2]').text
            transfers = elem.find_element_by_xpath('td[5]').text
            trading = elem.find_element_by_xpath('td[6]').text
            windrawals = elem.find_element_by_xpath('td[7]').text
            print('token:', token, 'deposit:', deposit, 'transfers:', transfers, 'trading:', trading, 'windrawals:',
                  windrawals)
        except:
            pass

# parce_token()
