import sys
dictionary = {
    "А": "A", "Б": "B", "В": "V", "Г": "G",
    "Д": "D", "Е": "E", "Ё": "E", "Ж": "Zh",
    "З": "Z", "И": "I", "Й": "I", "К": "K",
    "Л": "L", "М": "M", "Н": "N", "О": "O",
    "П": "P", "Р": "R", "С": "S", "Т": "T",
    "У": "U", "Ф": "F", "Х": "Kh", "Ц": "Tc",
    "Ч": "Ch", "Ш": "Sh", "Щ": "Shch", "Ъ": "",
    "Ы": "Y", "Ь": "", "Э": "E", "Ю": "Iu", 
    "Я": "Ia"
}
lines = ''
result = ''
with open("cyrillic.txt", encoding="UTF-8") as file_in:
    for line in file_in:
        lines += line
for s in lines:
    char = dictionary.get(s.upper(), s)
    if s.islower():
        result += char.lower()
    elif s.isupper():
        result += char
    else:
        result += s
with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    file_out.writelines(result)

