L = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def solution(L, N, arr):
    e_val =  (0, 0)
    
    for idx, (p, k) in enumerate(arr):
        e_val = max(e_val, (k - p, -(idx + 1)))
    
    cakes = [0 for _ in range(L + 1)]
    for idx, (p, k) in enumerate(arr):
        for x in range(p, k + 1):
            if cakes[x] == 0:
                cakes[x] = idx + 1
                
    r_val = (0, 0)
    for idx in range(1, N + 1):
        r_val = max(r_val, (cakes.count(idx), -(idx)))
        
    return f"{-e_val[1]}\n{-r_val[1]}"

    
print(solution(L, N, arr))