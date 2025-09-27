n, r = map(int, input().split())
sals = [int(input()) for _ in range(n)]

def solution(n, r, sals):
    
    cnt_1, cnt_2 = 0, 0
    
    for sal in sals:
        op1 = sal + r
        op2 = sal * 2
        if op1 > op2:
            cnt_1 += 1
        elif op1 < op2:
            cnt_2 += 1
            
    if cnt_1 == cnt_2:
        return 0
    elif cnt_1 < cnt_2:
        return 2
    else:
        return 1
    

print(solution(n, r, sals))