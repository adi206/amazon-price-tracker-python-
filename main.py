import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_1?crid=328XMHGW2RNMK&dchild=1&keywords=iphone+mobiles+12&qid=1621763105&sprefix=iphone+mobiles+1%2Caps%2C225&sr=8-1"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
target_price = 70
email_adress = "adityavernekar98@gmail.com"

def trackprice():
    price = int(get_price())
    if price > target_price:
        diff = price-target_price
        print(f"still {diff} thousand expensive")
    else:
        print("cost decreased")
        send_mail()
        pass

def get_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_dealprice').get_text().strip()[2:4]
    print(title)
    print(price)
    return price

def send_mail():
    subject = "iphone 12 price has dropped"
    mailtext = "subject:"<subject>'\n\n'+url

    server =smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(email_adress, 'Izuku#05')
    server.sendmail(email_adress, email_adress, mailtext)
    pass

if __name__ == "__main__":
    trackprice()







