# Day 9

number = input()
# 문자열로 받기

sorted_number = sorted(number, reverse=True)

result = ''.join(sorted_number)

print(result)