n = int(input())
# dp[i] 높이가i인 피자탑을 분리시켰을 때 얻을 수 있는 최대 즐거움
# dp[i] = max( a*(i-a) + dp[a] + dp[i-a])
dp = [0] * 11
dp[1] = 0
dp[2] = 1
dp[3] = 3
for i in range(4,11):
        for j in range(1,(i//2)+1):
            dp[i] = max(dp[i],j*(i-j) + dp[j] + dp[i-j])
# print(dp)
print(dp[n])