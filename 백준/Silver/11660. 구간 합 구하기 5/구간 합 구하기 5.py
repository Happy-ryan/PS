n,m = map(int,input().split())
arr = [list(map(int,input().split())) for row in range(n)]
brr = [list(map(int,input().split())) for row in range(m)]
dp =[[0 for  col in range(n+1)] for row in range(n+1)]
# 누적합
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1]
# 구간 누적합을 구하기 위한 함수
def psum(row):
    sum = 0
    for i in range(row[0],row[2]+1):
        sum += dp[i][row[3]] - dp[i][row[1]-1]

    return sum        
for row in brr:
    print(psum(row))