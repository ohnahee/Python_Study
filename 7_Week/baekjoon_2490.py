# Day 37

# 0 == 배
# 1 == 등

yut_results = []

for _ in range(3):
    yut_results.append(list(map(int, input().split())))

for yut in yut_results:
    if yut.count(1) == 4:
        print("E")
    elif yut.count(0) == 4:
        print("D")
    elif yut.count(0) == 3 and yut.count(1) == 1:
        print("C")
    elif yut.count(0) == 2 and yut.count(1) == 2:
        print("B")
    elif yut.count(0) == 1 and yut.count(1) == 3:
        print("A")
