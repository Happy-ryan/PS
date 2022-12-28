def solution(n):
    answer = 0
    mod = 1000000007
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2 
    for k in range(3, n + 1):
        dp[k] = (1 * dp[k - 1] + 1 * dp[k - 2]) % mod
    answer = dp[n]
    return answer