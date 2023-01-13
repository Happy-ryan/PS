def solution(n, money):
    mod = int(1e9) + 7
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in money:
        for i in range(1, n + 1):
            if i - k >= 0:
                dp[i] += dp[i - k]
                dp[i] %= mod
    return dp[n]