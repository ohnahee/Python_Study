# Day 31

A, B, C = map(int, input().split())
money = 0

if A == B == C:
    money = 10000 + A * 1000
elif A != B and B != C and C != A:
    max_number = max(A, B, C)
    money = max_number * 100 
else:
    if A == B or A == C:
        money = 1000 + A * 100
    else:
        money = 1000 + B * 100

print(money)