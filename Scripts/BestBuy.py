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

options = Options()
options.headless = True
LOGGER.setLevel(logging.WARNING)
urllibLogger.setLevel(logging.WARNING)

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("--disable-extensions")
options.add_argument("test-type")
options.add_argument('--disable-blink-features=AutomationControlled')

class bestbuy:
    def __init__(self, email, password, link):
        self.email = getpass("Email:")
        self.password = getpass("Password:")
        self.link =  input("Link:")
        self.bot = webdriver.Chrome(options=options)

    def buy(self):
        bot = self.bot
        print(':: ITS IN STOCK LETSS GOOOOO ::')
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-lg'))).click()
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a'))).click()
        print(':: Buying ::')
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button'))).click()
        time.sleep(1)
        print(':: Logging in ::')
        email = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.ID, 'fld-e')))
        email.send_keys(self.email)
        password = bot.find_element_by_id('fld-p1')
        password.send_keys(self.password)
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button'))).click()
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ispu-card__switch'))).click()
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button'))).click()
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/button'))).click()
        print(':: Item Bought ::')

    def function1(self,targeturl):
        bot = self.bot
        bot.get(targeturl)

    def stockCheck(self):
        bot = self.bot
        isComplete = False
        while (isComplete == False):
            try:
                not bot.find_element_by_class_name('btn-disabled')
                print(':: Not yet Bro ::')
                bot.refresh()
            except:
                self.buy()
                break
                    
    def main(self):
        self.function1(self.link)
        self.stockCheck()

ed = bestbuy("test", "test", "test")
ed.main()