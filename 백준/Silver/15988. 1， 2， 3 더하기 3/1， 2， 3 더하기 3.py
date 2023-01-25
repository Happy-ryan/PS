dp = [0] *1000006
mod = 1000000009
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,1000006):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%mod

T = int(input())
for i in range(T):
    n = int(input())
    print(dp[n])