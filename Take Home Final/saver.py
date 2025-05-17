# import os
# import json

# def save_json(data, filename):
#     folder = os.path.dirname(filename)
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#     with open(filename, "w") as f:
#         json.dump(data, f)


# import os

# def save_data(date, currency, xml_data):
#     directory = f"data/{currency}"
#     os.makedirs(directory, exist_ok=True)
    
#     file_path = os.path.join(directory, f"{date}.xml")

#     with open(file_path, "w") as file:
#         file.write(xml_data)

#     print(f"Saved data for {date} ({currency})")


# import os
# import json
# import xml.etree.ElementTree as ET

# def save_data(date, currency, xml_data):
#     directory = f"data/{currency}"
#     os.makedirs(directory, exist_ok=True)

#     # Save XML
#     xml_path = os.path.join(directory, f"{date}.xml")
#     with open(xml_path, "w") as file:
#         file.write(xml_data)

#     # Convert XML to JSON and Save JSON
#     json_data = xml_to_json(xml_data)
#     json_path = os.path.join(directory, f"{date}.json")
#     with open(json_path, "w") as file:
#         json.dump(json_data, file, indent=4)

#     print(f"Saved data for {date} ({currency})")

# def xml_to_json(xml_data):
#     root = ET.fromstring(xml_data)
#     return {child.tag: child.text for child in root}


# import os
# import json
# import xml.etree.ElementTree as ET

# def save_data(date, currency, xml_data):
#     directory = f"data/{currency}"
#     os.makedirs(directory, exist_ok=True)

#     # Save XML
#     xml_path = os.path.join(directory, f"{date}.xml")
#     with open(xml_path, "w") as file:
#         file.write(xml_data)

#     # Convert XML to JSON and Save JSON
#     json_data = xml_to_json(xml_data)
#     json_path = os.path.join(directory, f"{date}.json")
#     with open(json_path, "w", encoding="utf-8") as file:
#         json.dump(json_data, file, indent=4)

#     print(f"Saved XML and JSON for {date} ({currency})")

# def xml_to_json(xml_data):
#     root = ET.fromstring(xml_data)
#     json_output = {"exchange_rates": {"@date": root.find("pubDate").text, "exchange_rate": []}}

#     for item in root.findall("item"):
#         json_output["exchange_rates"]["exchange_rate"].append({
#             "@to_currency": item.find("targetCurrency").text,
#             "rate": item.find("exchangeRate").text
#         })

#     return json_output


# import os
# import json
# import xml.etree.ElementTree as ET

# def save_data(date, currency, xml_data):
#     BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Currency Data")
#     directory = os.path.join(BASE_DIR, f"data/{currency}")

#     os.makedirs(directory, exist_ok=True)

#     # Save XML file
#     xml_path = os.path.join(directory, f"{date}.xml")
#     with open(xml_path, "w", encoding="utf-8") as file:
#         file.write(xml_data)

#     # Convert XML to JSON and Save JSON file
#     json_data = xml_to_json(xml_data)
#     json_path = os.path.join(directory, f"{date}.json")
#     with open(json_path, "w", encoding="utf-8") as file:
#         json.dump(json_data, file, indent=4)

#     print(f"Saved XML and JSON for {date} ({currency})")

# def xml_to_json(xml_data):
#     root = ET.fromstring(xml_data)
    
#     json_output = {"exchange_rates": {"@date": root.find("pubDate").text, "exchange_rate": []}}

#     for item in root.findall("item"):
#         json_output["exchange_rates"]["exchange_rate"].append({
#             "@to_currency": item.find("targetCurrency").text,
#             "rate": item.find("exchangeRate").text
#         })

#     return json_output


# import os
# import json
# import xml.etree.ElementTree as ET

# # Define the correct base directory
# BASE_DIR = os.path.join(os.getcwd(), "Currency Data")  # Save inside "Currency Data"

# def save_data(date, currency, xml_data):
#     directory = os.path.join(BASE_DIR, currency)  # Ensure each currency has its own subfolder
#     os.makedirs(directory, exist_ok=True)

#     # Save XML file
#     xml_path = os.path.join(directory, f"{date}.xml")
#     with open(xml_path, "w", encoding="utf-8") as file:
#         file.write(xml_data)

#     # Convert XML to JSON and Save JSON file
#     json_data = xml_to_json(xml_data)

#     # Debugging print to verify JSON structure
#     print(f"Saving JSON for {currency} on {date}:")
#     print(json.dumps(json_data, indent=4))

#     json_path = os.path.join(directory, f"{date}.json")
#     with open(json_path, "w", encoding="utf-8") as file:
#         json.dump(json_data, file, indent=4)

#     print(f"Saved XML and JSON for {date} ({currency}) in {directory}")

# def xml_to_json(xml_data):
#     root = ET.fromstring(xml_data)
    
#     # Ensure JSON starts with {}
#     json_output = {
#         "exchange_rates": {
#             "@date": root.find("pubDate").text if root.find("pubDate") is not None else "Unknown",
#             "exchange_rate": []
#         }
#     }

#     # Extract exchange rates
#     for item in root.findall("item"):
#         to_currency = item.find("targetCurrency")
#         rate = item.find("exchangeRate")
        
#         if to_currency is not None and rate is not None:
#             json_output["exchange_rates"]["exchange_rate"].append({
#                 "@to_currency": to_currency.text,
#                 "rate": rate.text
#             })

#     # Debugging print to verify extracted exchange rates
#     print(f"Extracted exchange rates: {json_output['exchange_rates']['exchange_rate']}")

#     return json_output


# import os
# import json

# def save_json(data, filename):
#     folder = os.path.dirname(filename)
#     if not os.path.exists(folder):
#         os.makedirs(folder)  # create directory if missing

#     try:
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=4)  # pretty print json
#     except Exception as e:
#         print(f"Error saving file {filename}: {e}")

# import json
# import os

# def save_json(data, filename):
#     folder = os.path.dirname(filename)
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)

import os
import json
import xml.etree.ElementTree as ET

# Define the base directory
BASE_DIR = os.path.join(os.getcwd(), "Take Home Final/Data")

def save_data(date, currency, xml_data):
    directory = os.path.join(BASE_DIR, currency)  # Store data in subfolders
    os.makedirs(directory, exist_ok=True)

    json_data = xml_to_json(xml_data)

    if json_data:  # Ensure valid JSON data before saving
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

    return json_output if json_output["exchange_rates"]["exchange_rate"] else None  # Ensure JSON contains data
