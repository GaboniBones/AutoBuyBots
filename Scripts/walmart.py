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
options.headless = True
LOGGER.setLevel(logging.WARNING)
urllibLogger.setLevel(logging.WARNING)

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("--disable-extensions")
options.add_argument("test-type")
options.add_argument('--disable-blink-features=AutomationControlled')




class walmart:
    def __init__(self,email,password,link):
        self.email = input('Email:')
        self.password = input('Password:')
        self.link = input('Product Link:')
        self.bot = bot(options=options)




        