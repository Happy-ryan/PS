row,col = map(int,input().split())
arr = [list(map(int,input().split())) for row in range(row)]
# print(arr)
dp = [[0 for col in range(col)] for row in range(row)]
for i in range(row):
    for j in range(col):
        dp[i][j] = arr[i][j]+max(dp[i-1][j],dp[i][j-1])

print(dp[row-1][col-1])