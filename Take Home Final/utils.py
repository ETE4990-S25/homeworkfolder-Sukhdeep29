# import random
# import os
# from datetime import datetime, timedelta

# rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY",
#          "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW",
#          "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN",
#          "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]

# def pick_random_base():
#     choices = []
#     for r in rates:
#         if r != "USD" and r != "EUR" and r != "GBP":
#             choices.append(r)
#     return random.choice(choices)

# def get_all_dates(start):
#     dates = []
#     today = datetime.today()
#     d = datetime.strptime(start, "%Y-%m-%d")
#     while d <= today:
#         dates.append(d.strftime("%Y-%m-%d"))
#         d += timedelta(days=1)
#     return dates

# def make_url(date, base):
#     return "https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date=" + date + "&base_currency_code=" + base + "&format_type=xml"

# def make_filename(date, base):
#     return "data/" + base + "/" + date + "_exchange_rates.json"

# def already_downloaded(date, base):
#     file_path = make_filename(date, base)
#     return os.path.exists(file_path)

# import os
# import random
# from datetime import datetime, timedelta

# def get_all_dates(start_date):
#     start = datetime.strptime(start_date, "%Y-%m-%d")
#     end = datetime.today()
#     delta = timedelta(days=1)
#     dates = []
#     while start <= end:
#         dates.append(start.strftime("%Y-%m-%d"))
#         start += delta
#     return dates

# def pick_random_base():
#     currencies = ["USD", "EUR", "GBP", "JPY", "AUD"]
#     return random.choice(currencies)

# def was_already_downloaded(date, currency):
#     return os.path.exists(f"data/{currency}/{date}.xml") 

import os
import random
from datetime import datetime, timedelta

def get_all_dates(start_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.today()
    delta = timedelta(days=1)
    dates = []
    while start <= end:
        dates.append(start.strftime("%Y-%m-%d"))
        start += delta
    return dates

def pick_random_base():
    currencies = ["USD", "EUR", "GBP", "JPY", "AUD"]
    return random.choice(currencies)

def was_already_downloaded(date, currency):
    return os.path.exists(f"data/{currency}/{date}.json")  # Check if JSON exists