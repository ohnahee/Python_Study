import math

A = int(input())

for _ in range(A):
    N, M = map(int, input().split())
    if N == M:
        print(1)
    else:
        print(math.comb(M, N))
