N = int(input())

def solution(N):
    
    if N < 10:
        return 99
    
    l = len(str(N))
    
    num = 10 ** l
    
    tmp = [N]
    
    answer = N
    
    for i in range(num):
        n1 = N - i
        n2 = N + i
        
        if n1 > 0 and n1 % 10 == 9 and n1 % 100 == 99:
            tmp.append(n1)
            
        if n2 >0 and n2 % 10 == 9 and n2 % 100 == 99:
            tmp.append(n2)
            
    tmp.sort()
    
    idx = tmp.index(N)
    
    if idx == 0:
        return tmp[idx + 1]
    else:
        if N - tmp[idx - 1] >= tmp[idx + 1] - N:
            return tmp[idx + 1]
        else:
            return tmp[idx - 1]

print(solution(N))