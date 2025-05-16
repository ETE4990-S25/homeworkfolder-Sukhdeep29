import os
import json

def save_json(data, filename):
    folder = os.path.dirname(filename)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(filename, "w") as f:
        json.dump(data, f)