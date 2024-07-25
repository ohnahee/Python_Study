# Day 8

num_of_seminars = 7
seminars = []

for i in range(num_of_seminars):
    seminar_name, applicants = input().split()
    seminars.append((seminar_name, int(applicants)))

max_seminar = seminars[0]
# 최대 세미나의 수를 0번째로 초기화 해준다

for seminar in seminars:
    if seminar[1] > max_seminar[1]:
        max_seminar = seminar


print(max_seminar[0])
