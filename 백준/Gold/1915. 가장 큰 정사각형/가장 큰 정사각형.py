import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input()) for row in range(n)]

def solution(mat):
    ans = 0

    dp = [[0 for col in range(m)] for row in range(n)]
    
    for r in range(n):
        dp[r][0] = int(mat[r][0])

    for c in range(m):
        dp[0][c] = int(mat[0][c])

    for r in range(1, n):
        for c in range(1, m):
            if int(mat[r][c]) == 0: 
                continue

            dp[r][c] = 1 + min(int(dp[r - 1][c - 1]),\
                            int(dp[r - 1][c]),\
                            int(dp[r][c - 1]))
            
    for i in range(n):
        for j in range(m):
            ans = max(ans, dp[i][j])

    return ans

print(solution(mat)**2)