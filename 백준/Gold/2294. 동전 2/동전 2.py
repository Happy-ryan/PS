# https://www.acmicpc.net/problem/2294
# 동전의 값이 서로 배수 관계가 아니므로 그리디 불가능
# 점화식 정의하는 것이 포인트..

n, k = map(int, input().split())
moneys = [ int(input()) for _ in range(n)]

inf = int(1e18)
dp = [inf] * (k + 1)

for money in moneys:
    if money > k:
        continue

    dp[money] = 1
    
for i in range(1, k + 1):
    for money in moneys:
        
        if i >= money:
            dp[i] = min(dp[i], dp[i - money] + 1)
            

if dp[k] >= inf:
    print(-1)
else:
    print(dp[k])   