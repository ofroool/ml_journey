import json
from pprint import pprint

with open("data.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
pprint(records)