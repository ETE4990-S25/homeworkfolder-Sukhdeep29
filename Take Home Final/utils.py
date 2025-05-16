import random
import os
from datetime import datetime, timedelta

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY",
         "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW",
         "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN",
         "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]

def pick_random_base():
    choices = []
    for r in rates:
        if r != "USD" and r != "EUR" and r != "GBP":
            choices.append(r)
    return random.choice(choices)

def get_all_dates(start):
    dates = []
    today = datetime.today()
    d = datetime.strptime(start, "%Y-%m-%d")
    while d <= today:
        dates.append(d.strftime("%Y-%m-%d"))
        d += timedelta(days=1)
    return dates

def make_url(date, base):
    return "https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date=" + date + "&base_currency_code=" + base + "&format_type=xml"

def make_filename(date, base):
    return "data/" + base + "/" + date + "_exchange_rates.json"

def already_downloaded(date, base):
    file_path = make_filename(date, base)
    return os.path.exists(file_path)