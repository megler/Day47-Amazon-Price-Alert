# Amazon Price Alerts

Python Bootcamp Day 47 - Amazon Price Checker


## Usage
Using the Amazon API via [Amazon_Paapi](https://python-amazon-paapi.readthedocs.io/en/latest/index.html) and [MailJet](https://app.mailjet.com/dashboard), check current price of desired item and if 
price is less than your trigger, send an email.

This is a quick one page script that checks the current price of a desired item
and emails you if the price is below your trigger amount.

This was originally going to be a web scrape project using Beautiful Soup, but
Amazon has anti-scraping tech that was more trouble than it was worth. Since I 
already had an Amazon Developer API and also an Amazon Affiliate Account, it was
pretty straightforward to use that instead.

The Amazon_Paapi module is great for converting API endoints into Python. One thing
to note using this module is it continues running once you run your script. To
stop, CTRL-C your terminal as a keyboard interrupt.

You can use the SMTP module to send email, but I wanted to have something to grow
with that already has inboxing resolved and is less hassle setting up. MailJet was
super easy to get started and reliably inboxed every time. They also have a 
generous free account to start with.

Environment Variables are saved in a .env file and called using [Python-Dotenv](https://pypi.org/project/python-dotenv/).

To install all modules used in this project you can use:

`pip install -r requirements.txt`

## License
[MIT](https://choosealicense.com/licenses/mit/)