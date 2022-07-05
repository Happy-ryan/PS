#dp[i] = i!(팩토리얼)값이다.
dp = [0]*101
dp[0] = 1 #0!=1 이다
dp[1] = 1
for i in range(2,101):
    dp[i] = i*dp[i-1]
# print(dp)
n,m = map(int,input().split())

p = dp[n]
q = dp[m]*dp[n-m]

print(p//q)