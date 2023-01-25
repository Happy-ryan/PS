n = int(input())
mod = 1000000000
dp = [[ 0 for col in range(11) ] for row in range(n+1)]
# print(dp)
#dp[i][j]  i : 자릿수 j : 숫자
for j in range(1,10):
    dp[1][j] = 1 # 1,2,3,4,...9 각 1개 = 왜냐하면 j가 숫자를 의미하므로 1씩 각각 써줘야한다. / dp[1] = 9 ,, dp[1][j] =1
# print(dp)
for i in range(2,n+1):
    for j in range(0,10):
        if j == 0:
            dp[i][j] = (dp[i-1][1])%mod #j가 0일 때는 앞자리에 1만 올 수 있다.
        elif j == 9:
            dp[i][j] = (dp[i-1][8])%mod #j가 9일 때는 앞자리에 8만 올 수 있다.
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%mod

print(sum(dp[n])%mod)