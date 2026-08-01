import json
filename = input()
fileout = input()
with open(filename) as file_in:
    numbers = [int(numb) for numb in file_in.read().split()]

stat = {
    "count": len(numbers),
    "positive_count": sum(x > 0 for x in numbers),
    "min": min(numbers),
    "max": max(numbers),
    "sum": sum(numbers),
    "average": round(sum(numbers) / len(numbers), 2)
}
with open(fileout, "w") as file_out:
    json.dump(stat, file_out, ensure_ascii=False, indent=2)
