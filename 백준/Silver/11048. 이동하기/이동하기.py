n, m = map(int,input().split())
arr = [list(map(int,input().split())) for row in range(n)] 
# print(arr)
#dp[i][j]일 때 갖을 수 있는 최대 사탕의 수 누적
dp = [ [0 for col in range(m+1)] for row in range(n+1)]
dp[0][0] = arr[0][0]

for j in range(1,m):
    dp[0][j] = arr[0][j] + dp[0][j-1]
for i in range(1,n):
    dp[i][0] = arr[i][0] + dp[i-1][0]
# print(dp)
for i in range(1,n): # n 행
    for j in range(1,m): # m 열
        dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])
# print(dp)
print(dp[n-1][m-1])