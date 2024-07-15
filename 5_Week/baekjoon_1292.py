# Day 28

number_list = []

for i in range(1, 1001):
    number_list.extend([i] * i)

A, B = map(int, input().split())

result = sum(number_list[A-1:B])

print(result)
