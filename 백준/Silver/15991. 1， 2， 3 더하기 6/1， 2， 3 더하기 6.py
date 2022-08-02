n = int(input())
arr = [int(input()) for _ in range(n)]
mod = 1000000009
dp = [0] *100001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
for i in range(4,100001):
    if i < 6:
        dp[i] = (dp[i-2]+dp[i-4])%mod
    else:
        dp[i] = (dp[i-2]+dp[i-4]+dp[i-6])%mod

for x in arr:
    print(dp[x])