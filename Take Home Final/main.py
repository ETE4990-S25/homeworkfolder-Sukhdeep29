# import threading
# from downloader import download_data
# from utils import get_all_dates, pick_random_base, already_downloaded

# dates = get_all_dates("2011-05-04")
# base = pick_random_base()

# threads = []

# def download_for_data(date):
#     if not already_downloaded(date, base):
#         print("Getting:", date)
#         download_data(date, base)
#     else:
#         print("Already have:", date)

# for date in dates:
#     t = threading.Thread(target= download_for_data, args=(date,))
#     threads.append(t)
#     t.start()
#     if len(threads) >= 10:
#         for t in threads:
#             t.join()
#         threads = []

# for t in threads:
#     t.join()


# import threading
# from downloader import download_data
# from utils import get_all_dates, pick_random_base, was_already_downloaded

# all_dates = get_all_dates("2011-05-04")
# base_currency = pick_random_base()

# threads = []

# def download_for_date(date):
#     if not was_already_downloaded(date, base_currency):
#         print("Getting:", date)
#         download_data(date, base_currency)
#     else:
#         print("Already have:", date)

# for date in all_dates:
#     t = threading.Thread(target=download_for_date, args=(date,))
#     threads.append(t)
#     t.start()
#     if len(threads) >= 10:
#         for t in threads:
#             t.join()
#         threads = []

# for t in threads:
#     t.join()


import threading
from downloader import download_data
from utils import get_all_dates, pick_random_base, was_already_downloaded

# Get all dates from the starting point
all_dates = get_all_dates("2011-05-04")
base_currency = pick_random_base()

threads = []

# Helper function for each thread
def download_for_date(date):
    if not was_already_downloaded(date, base_currency):
        print("Getting:", date)
        download_data(date, base_currency)
    else:
        print("Already have:", date)

# Use threads, but only 10 at a time
for date in all_dates:
    t = threading.Thread(target=download_for_date, args=(date,))
    threads.append(t)
    t.start()
    if len(threads) >= 10:
        for t in threads:
            t.join()
        threads = []

for t in threads:
    t.join()