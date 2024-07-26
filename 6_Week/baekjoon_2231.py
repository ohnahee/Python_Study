N = int(input().strip())

start = max(1, N - 9 * len(str(N)))

smallest = 0

for i in range(start, N):
    digit_sum = sum(int(digit) for digit in str(i))
    if i + digit_sum == N:
        smallest = i
        break

print(smallest)