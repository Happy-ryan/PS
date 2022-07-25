def f(n):
    dp = [[0 for col in range(10)] for row in range(n+1)]
    for j in range(10):
        dp[1][j] = 1
    for i in range(2,n+1):
        for j in range(10):
            for add in dp[i-1][j:]:
                dp[i][j] += add
    return sum(dp[n])

n = int(input())
for _ in range(n):
    x = int(input())
    print(f(x))