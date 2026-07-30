from sys import stdin
lines = [int(numbers) for line in stdin for numbers in line.split()]
print(sum(lines))

