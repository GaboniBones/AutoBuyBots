import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from urllib3.connectionpool import log as urllibLogger
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
from bs4 import BeautifulSoup
import requests

options = Options()
options.headless = False
LOGGER.setLevel(logging.WARNING)
urllibLogger.setLevel(logging.WARNING)

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("--disable-extensions")
options.add_argument("test-type")
options.add_argument('--disable-blink-features=AutomationControlled')

class target:
    def __init__(self, email, password, link):
        self.email = getpass("Email:")
        self.password = getpass("Password:")
        self.link =  input("Link:")
        self.bot = webdriver.Chrome(options=options)


    def function1(self,targeturl):
        bot = self.bot
        bot.get(targeturl)

    def buy(self):
        bot = self.bot
        bot.refresh()
        print(':: IN STOCK! ::')
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/button'))).click()





    def stockCheck(self):
        bot = self.bot
        status = "Sold out"
        url = self.link
        while True:
            productpage = requests.get(url).text.lower()
            outofstockstrings = ['Sold out','See similar items']
            if any(x in productpage for x in outofstockstrings):
                print('not yet bro')
            else:
                print('kys')

        
                


    def main(self):
        self.function1(self.link)
        self.stockCheck()





gz = target('test','test','test')
gz.main()

