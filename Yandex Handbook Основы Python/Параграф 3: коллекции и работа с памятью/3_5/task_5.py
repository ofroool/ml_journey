from sys import stdin
lines = [words for line in stdin.readlines() for words in line.split()]
outp = set()
for word in lines:
    if word.lower() == word.lower()[::-1]:
        outp.add(word)
print(*outp, sep='\n')
