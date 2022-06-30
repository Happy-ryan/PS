n,m = map(int,input().split())
dp = [[0 for col in range(1003)] for row in range(1003)]
# def f(x,y):
#     if x == 1 or y == 1:
#         return 1
#     else:
#         if dp[x][y] != 0:
#             return dp[x][y]
#         else:
#             dp[x][y] = f(x,y-1)+f(x-1,y-1)+f(x-1,y)
#             return dp[x][y]
# 재귀dp사용 - error 발생
for i in range(1,1003):
    dp[i][1] = 1
for j in range(1,1003):
    dp[1][j] = 1
for i in range(2,n+1):
    for j in range(2,m+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + dp[i-1][j]

print(dp[n][m]%1000000007)