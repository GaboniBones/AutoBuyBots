from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from urllib3.connectionpool import log as urllibLogger
import time

options = Options()
options.headless = True
LOGGER.setLevel(logging.WARNING)
urllibLogger.setLevel(logging.WARNING)

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("--disable-extensions")
options.add_argument("test-type")
options.add_argument('--disable-blink-features=AutomationControlled')

class ps5Bot:
    def __init__(self, username, password, link):
        self.username = input("Enter Email:")
        self.password = input("Enter Password:")
        self.link = input("Link to product:")
        self.bot = webdriver.Chrome(options=options)

    def buy(self):
        bot = self.bot
        print(":: Buying ::")
        buy = bot.find_element_by_id("buy-now-button")
        if buy.is_displayed():
            buy.click()
        print(":: Logging In! ::")
        email = bot.find_element_by_id("ap_email")
        if email.is_displayed():
            email.send_keys(self.username)
        continuebutton = bot.find_element_by_id("continue")
        if continuebutton.is_displayed():
            continuebutton.click()
        password = bot.find_element_by_id("ap_password")
        if password.is_displayed():
            password.send_keys(self.password)
        submit = bot.find_element_by_id("signInSubmit")
        if submit.is_displayed():
            submit.click()
        print(":: finishing up ::")
        place_order = bot.find_element_by_id("placeYourOrder")
        if place_order.is_displayed():
            place_order.click()
        print(":: ITEM BOUGHT! ::")
        time.sleep(1)
        bot.save_screenshot("Buy_page")
        bot.quit()


    def findStock(self):
        bot = self.bot
        el = bot.find_element_by_tag_name('body')
        str = el.text
        while True:
            bot.refresh()
            if (str.find("Currently unavailable.") != -0):
                print(":: ITS IN STOCK! ::")
                self.buy()
                break

    def function1(self,targeturl):
        bot = self.bot
        bot.get(targeturl)

    def main(self,link):
        self.function1(self.link)
        print(":: At Amazon ::")
        self.findStock()


ed = ps5Bot("test", "Test", "link")
ed.main("link")