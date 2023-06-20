# https://www.acmicpc.net/problem/20152

def solution(h, n):
    # 2차원 정사각 dp의 한 변의 길이
    k = abs(h - n) + 1
    dp = [[0 for col in range(k)] for row in range(k)]
    
    # h == n 이여도 1가지 경우다!
    if k == 1:
    	return 1

    for i in range(1, k):
        dp[i][0] = 1
        
    for r in range(1, k):
        for c in range(1, k):
            if r > c:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
            elif r == c:
                dp[r][c] = dp[r][c - 1]
                
    return dp[-1][-1]

h, n = map(int, input().split())

print(solution(h, n))