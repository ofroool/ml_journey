import json
file_1 = input()
file_2 = input()
with open(file_1, encoding="UTF-8") as file_in:
    records = json.load(file_in)
with open(file_2, encoding="UTF-8") as file_in:
    updates = json.load(file_in)
print(records)
print(updates)
result = {}
for user in records:
    result[user.pop('name')] = user
for user in updates:
    name = user.pop('name')
    if name not in result.keys():
        result[name] = user
    else:
        for key, value in user.items():
            if key in result[name]:
                result[name][key] = max(value, result[name][key]) 
            else:
                result[name][key] = value
                
with open(file_1, "w", encoding="UTF-8") as file_out:
    json.dump(result, file_out, ensure_ascii=False, indent=2, sort_keys=True)