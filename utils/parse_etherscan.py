from pathlib import Path

from asgiref.sync import sync_to_async
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create your tests here.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
