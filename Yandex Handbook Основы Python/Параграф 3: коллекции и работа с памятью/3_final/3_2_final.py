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

final_data = []
passed_tests = 0
for row in student_tests:
    for test in tests:
        if test['id'] == row['test_id']:  
            title = test['title']
            break
    flag = 'FALSE'  
    for attempt in test_attempts:
        if attempt['test_class_user_link_id'] == row['id']:
            if attempt['flag_is_finished'] == 'TRUE':
                passed_tests += 1
                flag = 'TRUE'
            break 
    date_obj = datetime.strptime(row['datetime_started'], "%d.%m.%Y %H:%M:%S")
    final_data.append((date_obj, title, flag))

print(f"{passed_tests}/{len(student_tests)}")
final_data_sorted = sorted(final_data, reverse=True)
for test in final_data_sorted:
    date_obj = test[0]
    title = test[1]
    flag = test[2]
    beautiful_date = date_obj.strftime("%d.%m.%y")
    print(f"{title} {beautiful_date} {flag}")