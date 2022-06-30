T = int(input())
for row in range(T):
    dp = [[0,0] for col in range(44)]
    n = int(input())
    dp[0] = [1,0]
    dp[1] = [0,1]
    for i in range(2,n+1):
        dp[i] = [dp[i-1][0] + dp[i-2][0],dp[i-1][1] + dp[i-2][1]]
    print(*dp[n])