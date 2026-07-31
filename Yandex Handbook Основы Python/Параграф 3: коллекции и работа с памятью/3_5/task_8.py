file1_name = input().strip()
file2_name = input().strip()
file_out_name = input().strip()

with open(file1_name, encoding="UTF-8") as file_in:
    first = set(file_in.read().split())
with open(file2_name, encoding="UTF-8") as file_in:
    second = set(file_in.read().split())
result = sorted(first ^ second)
with open(file_out_name, "w", encoding="UTF-8") as file_out:
    print(*result, sep='\n', file=file_out)