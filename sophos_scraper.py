"""
@author: https://github.com/Divyateja04
"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from enum import Enum

import requests
from requests.models import Response

import logging
import time
from colorama import Fore, Back, Style

import json

logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.DEBUG)
logging.info("---Starting---")

class Browser(Enum):
    Edge = 1
    Chromium = 2
    Firefox = 3

def login_into_sophos(user_name: str, pass_word: str) -> Response:
    headers = {
    'Origin': 'http://172.16.0.30:8090',
    'Connection': 'keep-alive',
    'Referer': 'http://172.16.0.30:8090/',
    }

    data = {
        'mode': '191',
        'username': user_name,
        'password': pass_word,
    }

    response = requests.post('http://172.16.0.30:8090/login.xml', headers=headers, data=data)
    return response

# Prints the data used and left for the day
def get_data_left(user_name: str, pass_word: str, browser: Browser) -> float|None:
    match browser:
        case Browser.Edge:
            options = EdgeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            driver = webdriver.ChromiumEdge(options=options)
        case Browser.Chromium:
            options = ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            driver = webdriver.Chrome(options=options)
        case Browser.Firefox:
            options = FirefoxOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            driver = webdriver.Firefox(options=options)

    driver.get("https://172.16.0.30/userportal/webpages/myaccount/index.jsp")

    output = None

    try:
        logging.info("Entering Username")
        
        # Wait until element is loaded
        username = WebDriverWait(driver, timeout=10.).until(EC.presence_of_element_located((By.ID, "username")))
        username.send_keys(user_name)
        

        logging.info("Entering Password")
        password = driver.find_element(By.ID, 'password')
        password.send_keys(pass_word + Keys.RETURN)
        

        logging.info("Finding elements")
        
        # Wait until page is loaded
        usage = WebDriverWait(driver, timeout=10.).until(EC.presence_of_element_located((By.CLASS_NAME, "tabletext")))
        usage = driver.find_elements(By.CLASS_NAME, 'tabletext')
        

        print(Fore.GREEN + "::> Data Used: " + usage[-2].text + Style.RESET_ALL)
        print(Fore.GREEN + "::> Data Left: " + usage[-1].text + Style.RESET_ALL)
        output = float(usage[-1].text[:-2])
        logging.info(f"Data used : {usage[-1].text[:-2]}")
    
    except Exception as e:
        logging.error(e)
    
    driver.quit()

    return output

if __name__ == "__main__":
    print(Style.RESET_ALL)
    print(f"""{Fore.BLUE}Choose the browser : {Fore.LIGHTGREEN_EX}
    1> Edge
    2> Chrome
    3> Firefox
    """)
    
    browser = int(input(Fore.CYAN + "Browser: "))
    match browser:
        case 1:
            browser = Browser.Edge
        case 2:
            browser = Browser.Chromium
        case 3:
            browser = Browser.Firefox
        case _:
            logging.error("Incorrect browser chosen")
            browser = Browser.Firefox
    print(Style.RESET_ALL)

    logging.info(f"Browser : {browser} chosen")
    with open("data.json") as f:
        data = json.load(f)
        get_data_left(data["username"], data["password"], browser)
        