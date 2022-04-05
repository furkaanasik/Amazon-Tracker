import Scraper
from Scraper import Scrap as Sc
import time

# VARIABLES
URL = "https://www.amazon.com.tr/JBLC100SIUBLK-C100-JBL-Kulak-Kulakl%C4%B1k/dp/B01DEWVZ2C/ref=sr_1_5?__mk_tr_TR=%C3" \
      "%85M%C3%85%C5%BD%C3%95%C3%91&crid=3B359DH5STAEZ&keywords=kulakl%C4%B1k&qid=1648578903&sprefix=kulakl%C4%B1k" \
      "%2Caps%2C122&sr=8-5 "
is_email = str(input("do you want a email yes[y] or no[n]= ")).lower() == "y" and True or False
is_sms = str(input("do you want a sms yes[y] or no[n]= ")).lower() == "y" and True or False

# Create Scraper
track_products = Sc(is_sms=is_sms, is_email=is_email, product_url=URL)

# Check product price every 5 seconds
while track_products.is_Track:
    track_products.check_price_from_url()
    time.sleep(5)

print("end.")

