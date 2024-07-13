# Day 25

T = int(input())

for _ in range(T):
    Y_total = 0
    K_total = 0

    for _ in range(9):
        Y, K = map(int, input().split())
        Y_total += Y
        K_total += K
    
    if Y_total > K_total:
        print("Yonsei")
    elif Y_total < K_total:
        print("Korea")
    else:
        print("Draw")
