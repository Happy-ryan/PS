n = int(input())
dp = [0] * 1000006
dp[1] = -1
dp[2] = 1
dp[3] = -1
dp[4] = 2
dp[5] = 1
dp[6] = 3
dp[7] = 2
dp[8] = 4
dp[9] = 3
dp[10] = 2
for i in range(11,1000001):
    dp[i] = min(1+dp[i-5],1+dp[i-2])
print(dp[n])