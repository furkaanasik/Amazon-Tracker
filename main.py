from Scraper import Scrap as Sc
import time

# VARIABLES
URL = "ENTER URL"  # Enter URL
is_email_text = "WRITE Y OR N LETTER"  # Do you want a email yes[y] or no[n]
is_sms_text = "WRITE Y OR N LETTER"  # Do you want a sms yes[y] or no[n]

is_email = is_email_text.lower() == "y" and True or False
is_sms = is_sms_text.lower() == "y" and True or False

# Create Scraper
track_products = Sc(is_sms=is_sms, is_email=is_email, product_url=URL)

# Check product price every 5 seconds
while track_products.is_Track:
    track_products.check_price_from_url()
    time.sleep(5)

print("end.")

