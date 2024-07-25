# Day 21

n = int(input())  

numbers = list(map(int, input().split())) 
check_number = int(input())  

count = numbers.count(check_number)
print(count)
