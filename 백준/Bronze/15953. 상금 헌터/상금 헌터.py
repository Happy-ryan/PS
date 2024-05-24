def solution(a, b):
    sum_val = 0
    if a == 1:
        sum_val += 5000000
    elif 1 < a <= 3:
        sum_val += 3000000
    elif 3 < a <= 6:
        sum_val +=  2000000
    elif 6 < a <= 10:
        sum_val +=  500000
    elif 10 < a <= 15:
        sum_val +=  300000
    elif 15 < a <= 21:
        sum_val += 100000
    else:
        sum_val += 0

    if b == 1:
        sum_val += 5120000
    elif 1 < b <= 3:
        sum_val += 2560000
    elif 3 < b <= 7:
        sum_val += 1280000
    elif 7 < b <= 15:
        sum_val += 640000
    elif 15 < b <= 31:
        sum_val += 320000
    else:
        sum_val +=  0
        
    return sum_val

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solution(a, b))