import threading
from downloader import download_data
from utils import get_all_dates, pick_random_base, already_downloaded

dates = get_all_dates("2011-05-04")
base = pick_random_base()

threads = []

def download_for_data(date):
    if not already_downloaded(date, base):
        print("Getting:", date)
        download_data(date, base)
    else:
        print("Already have:", date)

for date in dates:
    t = threading.Thread(target= download_for_data, args=(date,))
    threads.append(t)
    t.start()
    if len(threads) >= 10:
        for t in threads:
            t.join()
        threads = []

for t in threads:
    t.join()
