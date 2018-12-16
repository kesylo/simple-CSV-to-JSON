#!/usr/bin/env python3

import csv
import json

csv_file_path = "happyDB.csv"
json_file_path = "happyDB.json"

# Read the CSV and add the data to a dictionnary
data = {}
with open(csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for csv_row in csv_reader:
        hmid = csv_row["hmid"]
        data[hmid] = csv_row

# print(data)

# Add all this data to a root node (we want the root node to be HappyDB, because later we may have other DB like SadDB)
root = {}
root["HappyDB"] = data

# Write data to the Json file
with open(json_file_path, "w") as json_file:
    # write to file and do some indent
    json_file.write(json.dumps(root, indent=4))
    # 
