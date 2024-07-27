# Day 36

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    last_digit = A % 10  

    if last_digit == 0:
        print(10)
    
    elif last_digit in [1, 5, 6]:
        print(last_digit)
    
    else:
        # 숫자의 주기 이용
        exponent = B % 4
        
        if exponent == 0:
            exponent = 4
        
        result = (last_digit ** exponent) % 10
        
        print(result)
