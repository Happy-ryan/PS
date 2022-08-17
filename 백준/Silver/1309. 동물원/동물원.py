n = int(input())
mod = 9901
# dp[i][0] : i번째 칸에 아무도 없는 경우
# dp[i][1] : i번째 칸에 왼쪽 칸에 사자가 있는 경우
# dp[i][2] : i번째 칸에 오른쪽 칸에 사자가 있는 경우
dp = [[0 for col in range(3)] for row in range(n+1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
for i in range(2,n+1):
    dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%mod
    dp[i][1] = (dp[i-1][0]+dp[i-1][2])%mod
    dp[i][2] = (dp[i-1][0]+dp[i-1][1])%mod

# print(dp[4][0])
# print(dp[4][1])
# print(dp[4][2])
print(sum(dp[n])%mod)