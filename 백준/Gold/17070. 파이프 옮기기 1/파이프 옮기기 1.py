# https://www.acmicpc.net/problem/17070
# 방향이 존재하는 2차원 DP > r, c, 방향 : 3차원 접근 필요
from pprint import pprint

N = int(input())
board = [list(map(int, input().split())) for row in range(N)]

def check(r, c, board):
    N = len(board)
    return 0<= r < N and 0<= c < N and not board[r][c]

# s, e, dir 처음시작점, 처음도착점, 처음방향
def solution(s, e, dir, board):
    N = len(board)
    # [0, 0, 0] -> 가로 : 0, 세로 : 1, 대각선 : 2 -> 인덱스
    dp = [[ [0, 0, 0] for col in range(N)] for row in range(N)]
    dp[s][e][dir] = 1
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                continue
            # 가로
            if check(r, c - 1, board):
                dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]
            # 세로
            if check(r - 1, c, board):
                dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]
            # 대각선, 3개의 칸 체크해야함!!(주의)
            if check(r - 1, c - 1, board) and check(r - 1, c, board) and check(r, c - 1, board):
                dp[r][c][2] += dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]
    # pprint(dp)
    return dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]

print(solution(0, 1, 0, board))