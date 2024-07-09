# Day 21

day_hight, night_hight, height = int(input.split())
day_hight, night_hight, height = 0
day = 0
sum_hight = 0

while sum_hight >= height:
    day += 1
    sum_hight += day_hight

    if sum_hight >= height:
        break

    sum_hight -= night_hight


print(day)