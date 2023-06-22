# https://www.acmicpc.net/problem/4811
# dp, 카탈린수 문제에 해당함..;;
# 1, 1, 2, 5, 14, 42, 132..

def solution(k):
    # 2차원 정사각 dp의 한 변의 길이
    # k == 0일 때도 dp[0] = 1이어야함 
    # 따라서 한 변의 길이 + 1 이 되어야하 k == 0 일 때도 1이 될 수 있음.
    dp = [[0 for col in range(k + 1)] for row in range(k + 1)]

    for i in range(1, k + 1):
        dp[i][0] = 1
        
    for r in range(1, k + 1):
        for c in range(1, k + 1):
            if r > c:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
            elif r == c:
                dp[r][c] = dp[r][c - 1]
                
    return dp[-1][-1]


while True:
    k = int(input())
    if k == 0:
        break
    print(solution(k))