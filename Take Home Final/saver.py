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


import os
import json
import xml.etree.ElementTree as ET

def save_data(date, currency, xml_data):
    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Currency Data")
    directory = os.path.join(BASE_DIR, f"data/{currency}")

    os.makedirs(directory, exist_ok=True)

    # Save XML file
    xml_path = os.path.join(directory, f"{date}.xml")
    with open(xml_path, "w", encoding="utf-8") as file:
        file.write(xml_data)

    # Convert XML to JSON and Save JSON file
    json_data = xml_to_json(xml_data)
    json_path = os.path.join(directory, f"{date}.json")
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4)

    print(f"Saved XML and JSON for {date} ({currency})")

def xml_to_json(xml_data):
    root = ET.fromstring(xml_data)
    
    json_output = {"exchange_rates": {"@date": root.find("pubDate").text, "exchange_rate": []}}

    for item in root.findall("item"):
        json_output["exchange_rates"]["exchange_rate"].append({
            "@to_currency": item.find("targetCurrency").text,
            "rate": item.find("exchangeRate").text
        })

    return json_output