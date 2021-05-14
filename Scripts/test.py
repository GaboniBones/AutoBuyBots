import requests
from bs4 import BeautifulSoup
import time
from lxml import html
import boto3
import env
URL = input('Product Link:')

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
stock = soup.find(id='outOfStock')

while True:
    if soup.find(id='outOfStock'):
        print(':: Not Yet Bro ::')
    else:
        print(':: In Stock! ::')
        publish()
        break


def publish():
    sns_vlient

