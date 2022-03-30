class Scrap:
    def __init__(self, *, is_sms=False, is_email=False, product_url="", product_title="", product_price):
        self.is_email = is_email
        self.is_sms = is_sms
        self.product_url = product_url
        self.product_title = product_title
        self.product_price = product_price

    def __send_sms(self):
        pass

    def __send_email(self):
        pass

    def check_price_from_url(self):
        pass





