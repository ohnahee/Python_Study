# Day 2

# 한줄에 숫자를 받는 코드 

n = int(input())
numbers = input()

total_sum = 0

for i in range(n):
    total_sum += int(numbers[i])
    
print(total_sum)



'''
이건 하나씩 받는 코드

n = int(input())

total_sum = 0

for i in range(n):
    number = int(input())
    total_sum += number
    
print(total_sum)

'''