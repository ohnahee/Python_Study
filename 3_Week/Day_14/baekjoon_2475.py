number = list(map(int,input().split()))

check_number = (number[0]**2 + number[1]**2 + number[2]**2 + number[3]**2 + number[4]**2) % 10

print(int(check_number))