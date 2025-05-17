
import os
import json
import xml.etree.ElementTree as ET

BASE_DIR = os.path.join(os.getcwd(), "Take Home Final/Data")

def save_data(date, currency, xml_data):
    directory = os.path.join(BASE_DIR, currency) 
    os.makedirs(directory, exist_ok=True)

    json_data = xml_to_json(xml_data)

    if json_data: 
        json_path = os.path.join(directory, f"{date}.json")
        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)
        print(f"Saved JSON for {currency} on {date} in {directory}")
    else:
        print(f"Data error for {currency} on {date}, skipping save.")

def xml_to_json(xml_data):
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError:
        print("Error parsing XML data, skipping conversion.")
        return None

    json_output = {
        "exchange_rates": {
            "@date": root.find("pubDate").text if root.find("pubDate") else "Unknown",
            "exchange_rate": []
        }
    }

    for item in root.findall("item"):
        to_currency = item.find("targetCurrency")
        rate = item.find("exchangeRate")

        if to_currency is not None and rate is not None:
            json_output["exchange_rates"]["exchange_rate"].append({
                "@to_currency": to_currency.text,
                "rate": rate.text
            })

    return json_output if json_output["exchange_rates"]["exchange_rate"] else None  
