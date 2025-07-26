N, L = map(int, input().split())
Cs = list(map(int, input().split()))

def soltuion(N, L, Cs):
    dp = [0] * (N + 1)
        
    for i in range(1, N + 1):
        if i <= L:
            dp[i] = dp[i - 1] + Cs[i - 1]
            continue
        
        dp[i] = Cs[i - 1] + (dp[i - 1] - Cs[i - L - 1])
    
    cnt = 0
    for c in dp:
        if 129 <= c  and c <= 138:
            cnt += 1
            
    return cnt
    
print(soltuion(N, L, Cs))