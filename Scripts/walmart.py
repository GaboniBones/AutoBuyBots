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


options = Options()
options.headless = False
LOGGER.setLevel(logging.WARNING)
urllibLogger.setLevel(logging.WARNING)

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("--disable-extensions")
options.add_argument("test-type")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])




class walmart:
    def __init__(self,email,password,link):
        self.email = input('Email:')
        self.password = input('Password:')
        self.link = input('Product Link:')
        self.bot = webdriver.Chrome(options=options)

    def buy(self):
        bot = self.bot
        print (':: Its In Stock ::')
         WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-lg'))).click()


    def stockcheck(self):
        inStock = False
        bot = self.bot

        while (inStock == False):
            try:
                bot.find_element_by_class_name('prod-blitz-copy-message')
                print(':: Not Yet Bro ::')
                bot.refresh()
            except:
                self.buy()
                break



    def function1(self,targeturl):
        bot = self.bot
        bot.get(targeturl)

    def main(self):
        self.function1(self.link)
        self.stockcheck()


gz = walmart("self","self","test")
gz.main()
        


