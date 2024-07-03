import sys
input = sys.stdin.read

# 입력을 한 번에 읽기
data = input().split()

N = int(data[0])

heights = list(map(int, data[1:]))

count = 0
max_height = 0

for height in reversed(heights):
    if height > max_height:
        count += 1
        max_height = height

print(count)
