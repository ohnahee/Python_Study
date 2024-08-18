def max_moves(A, B, C):
    gap1 = B - A
    gap2 = C - B
    return max(gap1, gap2) - 1

A, B, C = map(int, input().split())
print(max_moves(A, B, C))
