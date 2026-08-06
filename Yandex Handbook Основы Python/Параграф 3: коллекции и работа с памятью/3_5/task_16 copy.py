import sys
search = " ".join(input().lower().split())
filenames = [name.strip() for name in sys.stdin]
found = False
for name in filenames:
    with open(name, 'r', encoding='UTF-8') as file_in:
        text = file_in.read()
        clean_text = " ".join(text.lower().split())
    if search in clean_text:
        print(name)
        found = True
if not found:
    print("404. Not Found")