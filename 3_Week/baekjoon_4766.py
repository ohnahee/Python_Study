# Day 15

tem = []

while True:
    value = float(input())
    if value == 999:
        break
    tem.append(value)

n = len(tem)

for i in range(n - 1):
    print(f"{tem[i + 1] - tem[i]:.2f}")
