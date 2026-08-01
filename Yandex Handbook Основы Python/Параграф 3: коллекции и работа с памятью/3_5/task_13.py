import json
from sys import stdin 
filename = input()
new_dict = {line.strip().split(' == ')[0]: line.strip().split(' == ')[1] for line in stdin}

with open(filename, encoding="UTF-8") as file_in:
    records = json.load(file_in)

records.update(new_dict)
with open(filename, "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2, sort_keys=True)