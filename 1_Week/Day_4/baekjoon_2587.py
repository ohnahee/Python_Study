import sys
input = sys.stdin.read

data = input().strip().split()

numbers = list(map(int, data))
numbers.sort()

average = sum(numbers) // len(numbers)
middle = numbers[2]

print(average)
print(middle)