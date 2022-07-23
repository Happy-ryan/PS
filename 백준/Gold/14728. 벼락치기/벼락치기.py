N,T = map(int,input().split())
arr = [list(map(int,input().split())) for row in range(N)]
dp = [[-1 for col in range(T+1)] for row in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    dp[i] = dp[i-1].copy()
    for j in range(T+1):
        jump = j + arr[i-1][0]
        if dp[i-1][j] >= 0 and jump <= T:
            dp[i][jump] = max(dp[i][jump],dp[i-1][j]+arr[i-1][1])

print(max(dp[N]))