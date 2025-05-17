
import requests
from saver import save_data

BASE_URL = "http://www.floatrates.com/daily/{}.xml"

def download_data(date, currency):
    url = BASE_URL.format(currency.lower())

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        save_data(date, currency, response.text)
    except requests.RequestException as e:
        print(f"Failed to get data for {currency} on {date}: {e}")