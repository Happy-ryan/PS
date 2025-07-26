n = int(input())
candis = [int(input()) for _ in range(n)]

def solution(n, candis):
    
    cnt = 0
    
    while True:
        max_num = max(candis)
        idx = candis.index(max_num)
        
        num = candis[0]
        if num == max_num:
            break
        
        candis[0] += 1
        candis[idx] -= 1
        cnt += 1
    
        # print(f"현재상태 : {candis}")
    
    try:
        candis[1:].index(candis[0])
        cnt += 1
    except:
        cnt += 0
        
    return cnt
        
print(solution(n, candis))