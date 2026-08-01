import sys
filename = input()
N = int(input())
data = []
with open(filename, encoding="UTF-8") as file_in:
    for line in file_in.readlines():
        data.append(line.rstrip())
for strok in data[-N:]:
    print(strok)
        
