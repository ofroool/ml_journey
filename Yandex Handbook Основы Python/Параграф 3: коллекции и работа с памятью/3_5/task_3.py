from sys import stdin
for i in stdin.readlines():
    if not i.startswith('#'):
        clean_line = i.split('#')[0]
        print(clean_line.rstrip('\n'))