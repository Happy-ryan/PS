n = int(input())
# dp[i] 사람이i명 있을 때 악수할 수 있는 수
# 내가 i번째 사람이라면 i-1과 악수를 할 수도 있고 안 할 수도 있다.
# 따라서 dp[i] = dp[i-1](i-1과 악수x) +dp[i-2](i-1과 악수o)
dp = [0]*(n+1)
dp[1] = 1 
dp[2] = 2
for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2])%10

print(dp[n])