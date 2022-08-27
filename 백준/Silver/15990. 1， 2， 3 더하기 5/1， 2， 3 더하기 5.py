T = int(input())
mod = 1000000009
# dp 정의
# dp[n][1] dp[n][2] dp[n][3]
# n을 만들 때 반드시 1 or 2 or 3으로 시작한다는 의미
# 연속된 수가 가능하지 않으므로 1로 시작했으면 n-1에서는 2와 3으로 시작하는 배열 필요

dp = [[0 for col in range(4)] for row in range(100005)]
dp[1][1], dp[1][2], dp[1][3] = 1, 0, 0
dp[2][1], dp[2][2], dp[2][3] = 0, 1, 0
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1
for i in range(4,100005):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3])%mod
    dp[i][2] = (dp[i-2][1] + dp[i-2][3])%mod
    dp[i][3] = (dp[i-3][1] + dp[i-3][2])%mod

for _ in range(T):  
    n = int(input())
    result = sum(dp[n])%mod
    print(result)