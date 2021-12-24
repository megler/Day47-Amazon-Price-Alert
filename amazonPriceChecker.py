# amazonPriceChecker.py
#
# Python Bootcamp Day 47 - Amazon Price Checker
# Usage:
#      Using the Amazon API via Amazon_Paapi and MailJet, check current price of
# desired item and if price is less than your trigger, send an email
#
# Marceia Egler December 24, 2021

import os
from dotenv import load_dotenv
from mailjet_rest import Client
from amazon_paapi import AmazonApi


load_dotenv()
MAILJET_API = os.getenv("MAILJET_API")
MAILJET_KEY = os.getenv("MAILJET_KEY")
AMAZON_KEY = os.getenv("AWSAccessKeyId")
AMAZON_SECRET = os.getenv("AWSSecretKey")
AMAZON_TAG = os.getenv("TAG")

# Get Amazon Info
url = "https://smile.amazon.com/Calphalon-Premier-Space-Saving-Nonstick/dp/B072NGDV46/"
amazon = AmazonApi(AMAZON_KEY, AMAZON_SECRET, AMAZON_TAG, "US")
item = amazon.get_items(url)[0]


# Get Item name
item_name = item.item_info.title.display_value
# Get current price
price = item.offers.listings[0].price.amount

# Send Email
if price < 500.00:
    mailjet = Client(auth=(MAILJET_API, MAILJET_KEY), version="v3.1")
    data = {
        "Messages": [
            {
                "From": {
                    "Email": "ENTER-FROM-EMAIL",
                    "Name": "ENTER-FROM NAME",
                },
                "To": [
                    {
                        "Email": "ENTER-EMAIL-RECIPIENT",
                        "Name": "ENTER-RECIPIENT-NAME",
                    }
                ],
                "Subject": "Price Drop At Amazon.",
                "TextPart": f"The {item_name} you've been waiting for has had a price drop! It's current price is {price}.\nYou can buy it at: {url}",
                "HTMLPart": f"<p>Hey There,</p><p>The {item_name} you've been waiting for has had a price drop! It's current price is {price}.</p><p>You can buy it at: {url}</p>",
                "CustomID": "AmazonPriceDrop",
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
