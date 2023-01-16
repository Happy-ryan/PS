# 주어진 동전으로 특정한 값 만들기 - 순서x한 경우, DP
n, k = map(int, input().split())
moneys = [ int(input()) for _ in range(n)]
# print(moneys)

dp = [0] * (k + 1)
dp[0] = 1

for money in moneys: # 순서가 없어야하므로 주어진 동전들을 깐다.
    for target in range(1, k + 1):
        if target >= money:
            dp[target] += dp[target - money]

print(dp[k])