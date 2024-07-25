# Day 3

n = int(input())
numbers = []

for i in range(n):
    num = int(input()) #리스트에 넣어질 변수 추가
    numbers.append(num) #append 함수 추가

numbers.sort()

for number in numbers:
    print(number)
