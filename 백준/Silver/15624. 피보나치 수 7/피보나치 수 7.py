n = int(input())
mod = 1000000007
dp = [0]*1000006
dp[0] = 0
dp[1] = 1
dp[2] = 1
for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2])%mod
print(dp[n])