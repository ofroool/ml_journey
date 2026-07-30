from sys import stdin
lines = [line.rstrip('\n') for line in stdin.readlines()]
flag = lines[-1].lower()
for i in lines[:-1]:
    if flag in i:
        print(i)
