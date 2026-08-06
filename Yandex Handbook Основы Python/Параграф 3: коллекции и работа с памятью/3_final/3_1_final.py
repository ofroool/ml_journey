import csv

with open("user.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data_user = list(reader)
data_len = []
data_len.append(len(data_user))

with open("class.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data_class = list(reader)
data_len.append(len(data_class))

with open("class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data_class_user_link = list(reader)
data_len.append(len(data_class_user_link))

with open("task.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    task = list(reader)
data_len.append(len(task))

with open("test.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    test = list(reader)
data_len.append(len(test))

with open("test_task_link.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    test_task_link = list(reader)
data_len.append(len(test_task_link))

with open("test_class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    test_class_user_link = list(reader)
data_len.append(len(test_class_user_link))

with open("test_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    test_attempt = list(reader)
data_len.append(len(test_attempt))

with open("task_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    task_attempt = list(reader)
data_len.append(len(task_attempt))

print(*data_len, sep=' ')