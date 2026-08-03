from sys import stdin
import json
with open("task_15.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
print(records)
total_points = 0
answers = [x.rstrip() for x in stdin]
print(answers)
i = 0
for group in records:
    all_points = group['points']
    tests = len(group['tests'])
    group_costs = all_points // tests
    
    for test in group['tests']:
        if test['pattern'] == answers[i]:
            total_points += group_costs
        i += 1
print(total_points)