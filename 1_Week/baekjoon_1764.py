# Day 2

import sys

#sys.stdin.readline 이라는 이름으로 input 사용하자 개 기니까
input = sys.stdin.readline

n, m = map(int, input().split())

A = set()
B = set()

for i in range(n):
    A.add(sys.stdin.readline().rstrip())
for i in range(m):
    B.add(sys.stdin.readline().rstrip())

C = sorted(A&B)


print(len(C))

for item in C:
    print(item)