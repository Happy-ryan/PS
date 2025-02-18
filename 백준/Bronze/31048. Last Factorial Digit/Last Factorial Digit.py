t = int(input())

dp = [0] * 11
dp[1] = 1
for i in range(2, 11):
    dp[i] = dp[i - 1] * i

for _ in range(t):
    n = int(input())
    print(dp[n] % 10)