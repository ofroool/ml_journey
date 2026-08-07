import csv
from datetime import datetime


def load_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


users = load_csv("user.csv")
classes = load_csv("class.csv")
class_user_links = load_csv("class_user_link.csv")
tasks = load_csv("task.csv")
tests = load_csv("test.csv")
test_task_links = load_csv("test_task_link.csv")
test_class_user_links = load_csv("test_class_user_link.csv")
test_attempts = load_csv("test_attempt.csv")
task_attempts = load_csv("task_attempt.csv")

user_id_input, class_id_input = input().split()

#получить id между классом и учеником
for row in class_user_links:
    if row['user_id'] == user_id_input and row['class_id'] == class_id_input:
        class_user_id = row['id']
        break

#получить test_id
student_tests = []
for row in test_class_user_links:
    if row['class_user_link_id'] == class_user_id:
        student_tests.append(row)
print(student_tests)

student_tests.sort(
    key=lambda row: datetime.strptime(row['datetime_started'], "%d.%m.%Y %H:%M:%S"), 
    reverse=True
)
latest_test = student_tests[0]
test_id = latest_test['test_id']
current_link_id = latest_test['id']
current_test_attempt_id = ''
for row in test_attempts:
    if row['test_class_user_link_id'] == current_link_id:
        current_test_attempt_id = row['id']
        break

test_info = []
for row in task_attempts:
    if row['test_attempt_id'] == current_test_attempt_id:
        test_info.append(row)
test_structure = []
for row in test_task_links:
    if row['test_id'] == test_id:
        test_structure.append(row)

test_structure.sort(key=lambda x: int(x['order_number']))
print(*test_structure)

final_data = []
task_passed = 0
tasks_answered = 0 
all_time = 0

for task_link in test_structure:
    current_task_id = task_link['task_id']
    order_number = task_link['order_number']
    current_answer = ''
    for task in tasks:
        if task['id'] == current_task_id:
            current_answer = task['correct_answer']
            break  
    
    student_answer = None  
    spent_time = 0
    for attempt in test_info:
        if attempt['task_id'] == current_task_id:
            student_answer = attempt['answer']
            spent_time = int(attempt['time_spent'])  
            break
            
    if student_answer is None or student_answer == '':
        flag = '?'
    else:
        tasks_answered += 1  
        if student_answer == current_answer:
            task_passed += 1
            flag = 'TRUE'
        else:
            flag = 'FALSE'
            
    all_time += spent_time
    final_data.append((order_number, flag, current_task_id))

amount_tasks = len(test_structure)
if amount_tasks > 0:
    percent_completed = (tasks_answered / amount_tasks) * 100
else:
    percent_completed = 0.0
if tasks_answered > 0:
    percent_correct = (task_passed / tasks_answered) * 100
else:
    percent_correct = 0.0

p1_str = str(round(percent_completed, 1)).replace('.', ',') + '%'
p2_str = str(round(percent_correct, 1)).replace('.', ',') + '%'

print(f"{p1_str} {p2_str}")
for item in final_data:
    print(f"{item[0]} {item[1]} {item[2]}")

hours = all_time // 3600
minutes = (all_time % 3600) // 60
seconds = all_time % 60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")