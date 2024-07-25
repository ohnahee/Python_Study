# Day 18

A, B, C = list(map(int, input().split()))

middle_number = 0

if A == B == C:
    middle_number = A
elif A == B or A == C:
    middle_number = A
elif B == C:
    middle_number = B
elif (A > B and A < C) or (A > C and A < B):
    middle_number = A
elif (B > A and B < C) or (B > C and B < A):
    middle_number = B
else:
    middle_number = C

print(middle_number)



'''

A, B, C = list(map(int, input().split()))

middle_number = 0

if (A > B and A < C) or (A < B and A > C):
    middle_number = A
elif (B > A and B < C) or (B < A and B > C):
    middle_number = B
elif (A==C)or(A==B):
    middle_number = A
elif (B==C)or(B==C):
    middle_number = B
elif (C==A)or(C==B):
    middle_number = C
else:
    middle_number = C

print(middle_number)


'''



