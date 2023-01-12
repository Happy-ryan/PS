n = int(input())
board = [list(map(int, input().split())) for row in range(n)]
dp = [[0] * n for row in range(n)]
# (0,0)에서 (i,j)까지의 경우의 수
dp[0][0] = 1

for r in range(0, n):
    for c in range(0, n):
        for k in range(0, n):
            if 0 <= r - k and k == board[r - k][c]:
                dp[r][c] += dp[r - k][c]
            if 0 <= c - k and k == board[r][c - k]:
                dp[r][c] += dp[r][c - k]


print(dp[n - 1][n - 1])