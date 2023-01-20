# 2차원 DP
def solution(land):
    answer = 0
    R = len(land)
    dp = [[0 for col in range(4)] for row in range(R)]
    dp[0][0], dp[0][1], dp[0][2], dp[0][3] = land[0]
    for i in range(1, R):
        for j in range(0, 4):
            if j == 0:
                dp[i][j] = land[i][j] + max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]) 
            elif j == 1:
                dp[i][j] = land[i][j] + max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3]) 
            elif j ==  2:
                dp[i][j] = land[i][j] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3]) 
            else:
                dp[i][j] = land[i][j] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) 
    return max(dp[R - 1])