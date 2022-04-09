import requests
import os
import smtplib
from twilio.rest import Client
from bs4 import BeautifulSoup as Bs
from dotenv import load_dotenv


class Scrap:
    is_Track = True

    def __init__(self, *, is_sms=False, is_email=False, product_url=""):
        if is_email:
            self.email = str(input("Please enter your email = "))
        if is_sms:
            self.phone_number = str(input("Please enter your phone number = "))

        self.product_title = None
        self.product_price = None
        self.soup = None
        self.tracker_price = 0
        self.is_email = is_email
        self.is_sms = is_sms
        self.product_url = product_url

    # Send request link
    def request_url(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/99.0.4844.82 Safari/537.36"}
        page = requests.get(self.product_url, headers=headers)
        soup = Bs(page.content, 'html.parser')
        self.soup = soup
        # Scrap product title and price
        self.scrap_title_and_price()

    # Scrap product title and price
    def scrap_title_and_price(self):
        # FIND TITLE and PRICE VARIABLE
        self.product_title = self.soup.find(id="productTitle").text.strip()
        self.product_price = int(self.soup.find("span", {"class": "a-offscreen"})
                                 .text.replace(",", "").replace("TL", ""))
        print("-" * len(self.product_title))
        print("Product Name = ", self.product_title)
        print("Product Price = ", self.product_price)
        print("-" * len(self.product_title))
        self.tracker_price = int(input("Please enter the price you want to track =  "))

    # Check product price. if tracking price is bigger than product price send email or sms.
    def check_price_from_url(self):
        self.request_url()
        if self.is_Track:
            self.product_price = int(self.soup.find("span", {"class": "a-offscreen"})
                                     .text.replace(",", "").replace("TL", ""))
            if self.tracker_price > self.product_price:
                if self.is_sms:
                    self.send_sms()

                if self.is_email:
                    self.send_email()

                self.is_Track = False

    # Send sms
    def send_sms(self):
        load_dotenv()
        """
        client = Client(os.getenv("account_sid"), os.getenv("auth_token"))
        client.messages.create(
            body=f"{self.product_title} product has dropped below {self.tracker_price}!",
            from_=os.getenv("twilio_number"),
            to=self.phone_number
        )
        """
        print("sms")

    # Send email
    def send_email(self):
        load_dotenv()

        sender = os.getenv("email")
        subject = "Amazon Product Tracker"
        body = f"{self.product_title} product has dropped below {self.tracker_price}!"

        message = 'Subject: {}\n\n{}'.format(subject, body).encode("utf-8")

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        try:
            server.login(sender, os.getenv("email_password"))
            server.sendmail(sender, self.email, message)
            print("Email has been send!")
        except smtplib.SMTPAuthenticationError:
            print("unable to sign in")
