# https://www.acmicpc.net/problem/1937

import sys
sys.setrecursionlimit(10**5)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
# 시작점이 정해진 문제는 아님. 따라서 시작점의 조건을 잘 설정해야함.
# dpf(r, c) = max(dpf(pre_r, pre_c) + 1, ret) 
# where board[pre_r][pre_c] < board[r][c]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def dpf(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    
    ret = 0
    is_start = True
    for k in range(4):
        pre_r, pre_c = r + dr[k], c + dc[k]
        if in_range(pre_r, pre_c) and board[r][c] > board[pre_r][pre_c]:
            is_start = False
            ret = max(ret, dpf(pre_r, pre_c) + 1)
    # 시작점에서는 가장 작은 대나무가 들어야간다
    # 따라서 for문 돌 때 만족할 수 없다.
    if  is_start:
        return 1
    
    dp[r][c] = ret
    
    return ret


max_ans = 0
for i in range(n):
    for j in range(n):
        max_ans = max(max_ans, dpf(i, j))
        
print(max_ans)