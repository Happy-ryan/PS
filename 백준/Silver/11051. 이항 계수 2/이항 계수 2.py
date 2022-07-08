n, k = map(int,input().split())
mod = 10007
# dp[i] 숫자i까지의 팩토리얼 값 의미
dp = [0]*1000006
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    dp[i] = i*dp[i-1]

p = dp[n]
q = dp[k]*dp[n-k]

print((p//q)%mod)