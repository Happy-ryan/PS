N, L, W, H = map(int, input().split())

def solution(N, L, W, H):
    
    bs = int(1e9)
    
    L *= bs
    W *= bs
    H *= bs
    
    def cal(A):
        
        l = L // A
        w = W // A
        h = H // A
        
        return l * w * h
    
    inf = int(1e30) + 1
    l, r = 0, inf
    while l <= r:
        m = (l + r) // 2
        if cal(m) < N:
            r = m - 1
        else:
            l = m + 1
            
    return r / bs

print(solution(N, L, W, H))