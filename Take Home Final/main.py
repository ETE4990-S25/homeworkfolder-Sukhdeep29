
import os
import threading
from downloader import download_data
from utils import get_all_dates, was_already_downloaded

currencies = ["USD", "EUR", "GBP", "JPY", "CNY"]
all_dates = get_all_dates("2011-05-04")

threads = []

def download_for_currency(currency):
    for date in all_dates:
        if not was_already_downloaded(date, currency):
            print(f"Getting data for {currency} on {date}")
            download_data(date, currency)
        else:
            print(f"Already have data for {currency} on {date}")

for currency in currencies:
    t = threading.Thread(target=download_for_currency, args=(currency,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()