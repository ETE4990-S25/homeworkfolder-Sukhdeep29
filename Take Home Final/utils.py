
import os
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

def was_already_downloaded(date, currency):
    folder = os.path.join(os.getcwd(), "Take Home Final/Data", currency)
    json_path = os.path.join(folder, f"{date}.json")
    return os.path.exists(json_path) 
