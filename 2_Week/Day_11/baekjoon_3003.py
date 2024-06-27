#킹1, 퀸1, 룩2, 비숍2, 나이트2, 폰8

required = [1, 1, 2, 2, 2, 8]

chess = list(map(int, input().split()))

for i in range(len(required)):
    differences = required[i] - chess[i]
    print(differences, end=' ')