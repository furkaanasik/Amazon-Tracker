# Amazon Product Tracker
Welcome! this repository was created to track product price drop from amazon

## About The Project
In this project, it allows you to determine the maximum price of the product you want and receive sms or e-mail when this price drops.

Here's why:
 - List item
 - It allows you to be notified quickly when the price of a product drops.
 - You can set the maximum price of your product as you wish.
 - The information that the product price has decreased is sent to you by sms or e-mail.
 
 ## Used Packages
1. Time
    - `pip install python-time`
2. requests
    - `pip install requests`
3. BeautifulSoup
    - `pip install beautifulsoup4`
4. dotenv
    - `pip install python-dotenv`
 
## Getting Started
To run this program:
 1. Download source code.
 2.  Set the URL, is_email_text and is_sms_text variables. if is_email_text or is_sms_text is equal "y" letter it means yes.
 3. Enter your own email address in the email variable in the .env file.
 4. Enter your email password in the email_password authentication in the .env. This will allow you to send an e-mail to yourself when the price drops. If you wish, you can examine the send_email function in the Scraper.py file.
 5. Type your own number into the phone_number variable in the .env.
 6. Run this code on the server-side.

## Contact
Furkan Aşık - furkaanasik@gmail.com
