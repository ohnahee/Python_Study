# Day 20

time = []
for _ in range(4):
    time.append(int(input().strip()))

total_seconds = sum(time)

minutes = total_seconds // 60
seconds = total_seconds % 60

print(minutes)
print(seconds)