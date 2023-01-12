def solution(m, n, puddles):
    inf = int(1e18)
    mod = 1000000007
    # dp[i][j] = (0, 0)에서 (i, j)까지의 경우의 수
    # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    # 물웅덩이의 좌표 r, c라면 dp[r][c] == 0으로 더해져도 영향 주지 않도록 한다.
    dp = [[inf for col in range(m)] for row in range(n)]
    
    for row in puddles:
        dp[row[1] - 1][row[0] - 1] = 0
    
    dp[0][0] = 1
    
    for r in range(n):
        for c in range(m):
            if dp[r][c] == 0: 
                continue
            else:
                if 0<= r - 1 and c - 1 < 0:
                    dp[r][c] = (dp[r - 1][c]) % mod
                if 0<= c - 1 and r - 1 < 0:
                    dp[r][c] = (dp[r][c - 1]) % mod
                if 0<= r - 1 and 0<= c - 1:
                    dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % mod
                    
    answer = dp[n - 1][m - 1]
    return answer