# Day 24

a, b, c = map(int, input())
d, e, f = map(int, input())

abc = a * 100 + b * 10 + c
d_e_f = d * 100 + e * 10 + f

A = abc * f
B = abc * e
C = abc * d
D = A + (B * 10) + (C * 100)

print(A)
print(B)
print(C)
print(D)
