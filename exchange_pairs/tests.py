# import json
#
# import requests
# from django.test import TestCase
#
# from bs4 import BeautifulSoup
#
#
# # Create your tests here.
# # from exchange_comparison.utils import _query
#
#
# def set_new_token():
#     # url = 'https://api.hotbit.io/api/v1/asset.list'
#     url = 'https://api.1inch.exchange/v2.0/tokens'
#     response = requests.get(url=url)
#     jData = json.loads(response.content)['tokens']
#     for data in jData:
#         # print(jData[data])
#         token = jData[data]['symbol']
#         decimals = jData[data]['decimals']
#         contract = jData[data]['address']
#         row = f"INSERT INTO trusted_pairs(token, contract, decimals, is_active, tsymbol) VALUES ('{token}', '{contract}', {decimals}, 'f', '{token}') ON CONFLICT (token) DO UPDATE SET contract = '{contract}';"
#         # row = f"INSERT INTO trusted_pairs(token, contract, decimals, is_active, tsymbol) VALUES ('{token}', NULL, {decimals}, 'f', '{token}');"
#         print(row)
#         # resp = _query(row)
#         # print(resp)
#
#
# # set_new_token()
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_argument("start-maximized")
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-extensions")
# options.add_argument("--dns-prefetch-disable")
# options.add_argument("--window-size=1366,768")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
#
# driver = webdriver.Chrome(executable_path='../chromedriver.exe', chrome_options=options)
#
#
# class ModelReferences(object):
#     def init(self, driver, urls):
#         self.driver = driver
#         self.urls = urls
#
#     def get_html(self):
#         self.driver.get(self.urls)
#         return self.driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div/table/tbody/tr')
#
#
# def parce_token():
#     url = 'https://hitbtc.com/system-monitor'
#     driver.get(url)
#     elems = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div/table/tbody/tr')
#     # response = requests.get(url=url)
#     # contents = response.content
#     # soup = BeautifulSoup(contents, 'lxml')
#     for i, elem in enumerate(elems):
#         print(i)
#         try:
#             print('/******************')
#             token = elem.find_element_by_xpath('td[1]').text
#             deposit = elem.find_element_by_xpath('td[2]').text
#             transfers = elem.find_element_by_xpath('td[5]').text
#             trading = elem.find_element_by_xpath('td[6]').text
#             windrawals = elem.find_element_by_xpath('td[7]').text
#             print('token:', token, 'deposit:', deposit, 'transfers:', transfers, 'trading:', trading, 'windrawals:',
#                   windrawals)
#         except:
#             pass
#
# # parce_token()
