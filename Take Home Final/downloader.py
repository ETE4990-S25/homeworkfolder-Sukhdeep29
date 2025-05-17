# import requests
# import xmltodict
# import time
# from saver import save_json
# from utils import make_url, make_filename

# def download_data(date, base):
#     url = make_url(date, base)
#     try:
#         response = requests.get(url, timeout=10)
#         if response.status_code == 200:
#             data = xmltodict.parse(response.text)
#             filename = make_filename(date, base)
#             save_json(data, filename)
#         else:
#             print("Error getting data for", date)
#     except:
#         print("Problem getting data for", date)
#     time.sleep(0.5)


# import requests
# from saver import save_data

# BASE_URL = "http://www.floatrates.com/daily/{}.xml"

# def download_data(date, currency):
#     url = BASE_URL.format(currency.lower())
#     response = requests.get(url, timeout=10)

#     if response.status_code == 200:
#         save_data(date, currency, response.text)
#     else:
#         print(f"Failed to get data for {date}")

# import requests
# from saver import save_data

# BASE_URL = "http://www.floatrates.com/daily/{}.xml"

# def download_data(date, currency):
#     url = BASE_URL.format(currency.lower())
#     response = requests.get(url, timeout=10)

#     if response.status_code == 200:
#         save_data(date, currency, response.text)
#     else:
#         print(f"Failed to get data for {date}")

# 

# import requests
# import time
# from utils import make_url, make_filename
# from saver import save_json

# def download_data(date, base):
#     url = make_url(date, base)
#     filename = make_filename(date, base)
#     try:
#         response = requests.get(url, timeout=10)
#         if response.status_code == 200:
#             try:
#                 data = response.json()
#                 # Basic check for expected keys
#                 if "exchange_rates" not in data:
#                     print(f"Unexpected data format for {date} base {base}")
#                     print(f"Response snippet: {response.text[:300]}")
#                     return False
#                 save_json(data, filename)
#                 print(f"Saved data for {date} base {base}")
#                 return True
#             except Exception as e:
#                 print(f"JSON decode error for {date} base {base}: {e}")
#                 return False
#         else:
#             print(f"Error {response.status_code} for {date} base {base}")
#             return False
#     except Exception as e:
#         print(f"Download error for {date} base {base}: {e}")
#         return False
#     finally:
#         time.sleep(0.5)


import requests
from saver import save_data

BASE_URL = "http://www.floatrates.com/daily/{}.xml"

def download_data(date, currency):
    url = BASE_URL.format(currency.lower())

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error if request fails
        save_data(date, currency, response.text)
    except requests.RequestException as e:
        print(f"Failed to get data for {currency} on {date}: {e}")