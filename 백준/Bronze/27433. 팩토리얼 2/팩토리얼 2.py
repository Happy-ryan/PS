n = int(input())

def f(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]
    return dp[n]

print(f(n))