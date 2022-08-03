T = int(input())
arr = [list(map(int,input().split())) for _ in range(T)]

mod = 1000000009
# dp[i][j] 숫자i를 1,2,3의 합으로 나타내는데 사용한수가 j
# j의 max는 i를 만들기 위해서 1만 쓰는 경우 
dp = [[0 for col in range(1001)] for row in range(1001)]
dp[1][1] = 1 # 1을 만드는데 사용한 수의 갯수 1개 : 1
dp[2][1],dp[2][2] = 1,1 # 2를 만드는데 사용한 수의 갯수 1개 : 1
dp[3][1],dp[3][2],dp[3][3] = 1,2,1 # 3를 만드는데 사용한 수의 갯수 1개 : 1
# dp[i][j] = dp[i-1][j-1]+dp[i-2][j-1]+dp[i-3][j-1]
for i in range(4,1001):
    for j in range(2,i+1):
        if i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j-1]+dp[i-2][j-1]+dp[i-3][j-1])%mod
        
    
for row in arr:
    sum = 0
    for  j in range(row[1]+1):
        sum += dp[row[0]][j]
    print(sum%mod)