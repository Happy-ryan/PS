n,k = map(int,input().split())
arr = [list(map(int,input().split())) for row in range(n)]
# print(arr)
dp = [[-1 for col in range(k+1)] for row in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
    dp[i] = dp[i-1].copy()
    for j in range(k+1):
        if dp[i-1][j] >= 0 and j + arr[i-1][0] <= k:
            dp[i][j+arr[i-1][0]] = max(dp[i][j+arr[i-1][0]],dp[i-1][j]+arr[i-1][1])
print(max(dp[n]))