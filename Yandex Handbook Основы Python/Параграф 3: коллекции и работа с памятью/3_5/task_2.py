from sys import stdin
difference = [int(new) - int(old) for name, old, new in (line.split() for line in stdin)]
print(round(sum(difference) / len(difference)))