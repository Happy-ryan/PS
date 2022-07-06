n = int(input())
dp = [0]*1000006
dp[2] = 1
dp[3] = 1
# dp[4] = 2
# dp[5] = 3
# dp[6] = 2
# dp[7] = 3
# dp[8] = 3
# dp[9] = 2
for i in range(4,n+1):
    if i%2 == 0: # 짝수
        if i%3 ==0: # 2의배수&3의배수
            dp[i] = 1 + min(dp[i-1],dp[i//2],dp[i//3])
        else: #2의배수&3의배수x
            dp[i] = 1+ min(dp[i-1],dp[i//2])
    else: #홀수
        if i%3 == 0: #홀수&3의배수
            dp[i] = 1 + min(dp[i-1],dp[i//3])
        else: #홀수&3의배수x
            dp[i] = 1 + dp[i-1]
# print(dp)
print(dp[n])