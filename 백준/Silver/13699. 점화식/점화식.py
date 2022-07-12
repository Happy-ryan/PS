n = int(input())
# dp[i] = t(0)*t(i-1)+...+t(i-1)*t(0)
dp = [0] * 36
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    for j in (range(0,n)):
        dp[i] += dp[j]*dp[i-j-1]
print(dp[n])