import statistics 

numbers = []

for _ in range(10):
    line = input()
    numbers.append(int(line))

arr = sum(numbers) / len(numbers)

mode_numbers = statistics.mode(numbers)

print(int(arr))
print(mode_numbers)
