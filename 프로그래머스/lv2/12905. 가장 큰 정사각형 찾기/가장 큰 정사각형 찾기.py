def solution(board):
    ans = 0
    n, m = len(board), len(board[0])

    dp = [[0 for col in range(m)] for row in range(n)]
    
    for r in range(n):
        dp[r][0] = board[r][0]

    for c in range(m):
        dp[0][c] = board[0][c]

    for r in range(1, n):
        for c in range(1, m):
            
            if board[r][c] == 0: 
                continue

            dp[r][c] = 1 + min(dp[r - 1][c - 1],\
                            dp[r - 1][c],\
                            dp[r][c - 1])
            
    for i in range(n):
        for j in range(m):
            ans = max(ans, dp[i][j])

    return ans**2

