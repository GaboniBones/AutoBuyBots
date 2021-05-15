import requests
import twilio
from bs4 import BeautifulSoup
import time
from lxml import html
import os
from twilio.rest import  Client



URL = input('Product Link:')
number = input('Phone Number:')
account_sid = 'AC2d3bbab59fbb4261a7b87ee80d8e0a20'
auth_token =  'fd97b90adf062302c69d763d7a190727'
client = Client(account_sid, auth_token)






headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

def stockCheck():
    while True:
        if soup.find(id='outOfStock'):
            print(':: Not Yet Bro ::')
            time.sleep(1)
        else:
            print(':: In Stock! ::')
            publish()
            break


def publish():
   message = client.messages \
                .create(
                     body="The Product: " + URL + " Is in Stock BUY IT NOW",
                     from_='+14804057767',
                     to= number
                 )

stockCheck()



