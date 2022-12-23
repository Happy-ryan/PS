def solution(n):
    dp = [0]*(n+1)
    mod = 1234567
    
    dp[0], dp[1] = 0, 1
    for k in range(2, n+1):
        dp[k] = (dp[k-1] + dp[k-2])%mod
        
    answer = dp[n]
    return answer