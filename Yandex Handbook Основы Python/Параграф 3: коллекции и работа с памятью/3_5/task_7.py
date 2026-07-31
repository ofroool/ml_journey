import sys
filename = input()
with open(filename) as file_in:
    numbers = [int(numb) for numb in file_in.read().split()]
print(len(numbers))
print(sum(x > 0 for x in numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers), 2))