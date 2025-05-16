import requests
import xmltodict
import time
from saver import save_json
from utils import make_url, make_filename

def download_data(date, base):
    url = make_url(date, base)
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = xmltodict.parse(response.text)
            filename = make_filename(date, base)
            save_json(data, filename)
        else:
            print("Error getting data for", date)
    except:
        print("Problem getting data for", date)
    time.sleep(0.5)