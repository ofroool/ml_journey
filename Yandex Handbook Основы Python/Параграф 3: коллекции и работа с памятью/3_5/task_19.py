N = int(input())
with open('task_19.txt', 'r', encoding='UTF-8') as file_in:
    text = file_in.read()
with open('task_19_out.txt', 'w', encoding='UTF-8') as file_out:
    for s in text:
        if s.isupper():
            base = ord('A')
            s = chr((ord(s) - base + N) % 26 + base)
            print(s, end='', file=file_out)
        elif s.islower():
            base = ord('a')
            s = chr((ord(s) - base + N) % 26 + base)
            print(s, end='', file=file_out)  
        else:
            print(s, end='', file=file_out)