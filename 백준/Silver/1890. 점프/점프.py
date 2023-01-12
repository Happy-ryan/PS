n = int(input())
board = [list(map(int, input().split())) for row in range(n)]
dp = [[0] * n for row in range(n)]
# (0,0)에서 (i,j)까지의 경우의 수
dp[0][0] = 1

for r in range(0, n):
    for c in range(0, n):
        k = board[r][c]
        if k > 0 and r + k < n:
            dp[r + k][c] += dp[r][c]
        if k > 0 and c + k < n:
            dp[r][c + k] += dp[r][c]


print(dp[n - 1][n - 1])