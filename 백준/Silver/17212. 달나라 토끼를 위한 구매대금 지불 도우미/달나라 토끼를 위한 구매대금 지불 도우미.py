n = int(input())
dp = [0]*(1000006)
# dp[i] i원을 지불 하기 위한 동전의 최소 개수
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1
for i in range(8,n+1):
    dp[i] = min(1+dp[i-7],1+dp[i-5],1+dp[i-2],1+dp[i-1])
print(dp[n])