n = int(input())
mod = 10007
# dp[i][j] = 수의 길이가 i(row)일 때 마지막수(i번째수)가 j일 때 오르막수의 개수
dp =[[0 for col in range(10)] for row in range(n+1)]
for j in range(0,10):
    dp[1][j] = 1

for i in range(2,n+1):
    dp[i][9] = sum(dp[i-1])%mod
    for j in reversed(range(0,9)):
        dp[i][j] = (dp[i][j+1] - dp[i-1][j+1])%mod
print(sum(dp[n])%mod)