import requests
from bs4 import BeautifulSoup as Bs
from Scraper import Scrap as Sc

# VARIABLES
URL = "https://www.amazon.com.tr/JBLC100SIUBLK-C100-JBL-Kulak-Kulakl%C4%B1k/dp/B01DEWVZ2C/ref=sr_1_5?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3B359DH5STAEZ&keywords=kulakl%C4%B1k&qid=1648578903&sprefix=kulakl%C4%B1k%2Caps%2C122&sr=8-5"
email = str(input("do you want a email yes[y] or no[n]= ")).lower() == "y" and True or False
sms = str(input("do you want a sms yes[y] or no[n]= ")).lower() == "y" and True or False
tracker_price = int(input("Tracker Price = "))

# CONNECT URL and GET HTML CODE
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}
page = requests.get(URL, headers=headers)
soup = Bs(page.content, 'html.parser')

# FIND TITLE and PRICE VARIABLE
product_title = soup.find(id="productTitle").text.strip()
product_price = int(soup.find("span", {"class": "a-offscreen"}).text.replace(",", "").replace("TL", ""))

track_products = Sc(is_sms=sms, is_email=email, product_url=URL, product_title=product_title, product_price=product_price)

