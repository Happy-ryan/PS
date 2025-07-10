n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def solution(n, arr):
    
    inf = int(1e8)
    
    res = inf
    
    for row in arr:
        if sum(row) >= 512:
            res = min(res, sum(row))
    
    if res == inf:
        return -1
    
    return res

print(solution(n, arr))