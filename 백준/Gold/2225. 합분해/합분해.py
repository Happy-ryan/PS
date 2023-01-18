import sys, pprint
input = sys.stdin.readline

n, k = map(int, input().split())
mod = 1000000000

dp = [[0 for col in range(k + 1)] for row in range(n + 1)]

for j in range(k + 1):
    dp[0][j] = 1

for i in range(n + 1):
    dp[i][1] = 1


for i in range(1, n + 1):
    for j in range(2, k + 1):
        for x in range(0, i + 1):
            dp[i][j] += dp[x][j - 1]
            dp[i][j] %= mod


print(dp[n][k])