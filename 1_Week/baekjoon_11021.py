# Day 7

n = int(input())

for i in range(1, n+1): #1부터 n까지의 숫자를 차례대로 i에 대입하며 반복문 내부코드 실행
    numbers = list(map(int, input().split()))
    print("Case #%d: %d" % (i, numbers[0] + numbers[1]))
