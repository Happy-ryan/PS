k = int(input())
dp = [[0,0] for col in range(46)]
#dp[i] i번 눌렀을 때 [dp[i][0]=A의개수,dp[i][1] = B의개수]
dp[1] = [0,1]
dp[2] = [1,1]
# i번 눌렀을 때 A의 개수 : i-1번 눌렀을 때 B의 개수
# i번 눌렀을 때 B의 개수 : i-1번 눌렀을 때 A의개수 + B의개수 
for i in range(3,k+1):
    dp[i][0] += dp[i-1][1]
    dp[i][1] += dp[i-1][0]
    dp[i][1] += dp[i-1][1]
print(*dp[k])