student_scores = []

for i in range(5):    
    score = int(input()) #입력받는 변수
    student_scores.append(score) 

total = 0

for score in student_scores:  
    if score < 40:
        total += 40
    else:
        total += score

average = total // len(student_scores)

print(average)