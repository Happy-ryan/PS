#dp
def solution(n):
    answer = 0
    mod = 1234567
    dp = [0] * (n + 1)
    dp[1] = 1
    if n >= 2:
        dp[2] = 2
        for x in range(3, n + 1):
            dp[x] = (dp[x - 1] + dp[x - 2]) % mod
    return dp[n]