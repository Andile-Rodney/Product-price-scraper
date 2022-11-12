import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Digital-28-70mm/dp/B00FRDV06I/ref=sr_1_3?crid=2AZ92TRSHFZQ3&keywords=sony+a7&qid=1563390623&s=electronics&sprefix=sony+a7%2Celectronics%2C444&sr=1-3'

headers = {"User-Agent": Mozilla/5.0 (Windows NT 10.0, Win64, x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/75.0.3770.142 Safari/537.36}

headers = {'Cache-Control': 'no-cache', "Pragma": "no-cache"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")


    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip()) 

    if(converted_price < 1.700):
        send_mail()

def send_mail(): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('rodneymthunzi@gmail.com', '')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/Sony-Full-Frame-Mirrorless-Digital-28-70mm/dp/B00FRDV06I/ref=sr_1_3?crid=2AZ92TRSHFZQ3&keywords=sony+a7&qid=1563390623&s=electronics&sprefix=sony+a7%2Celectronics%2C444&sr=1-3'

    msg = f"Subject: {subject} \n\n{body}"

server.send_mail('rodneymthunzi@gmail.com',msg)
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while (True):
    check_price()
    time.sleep(1060)
