# https://www.acmicpc.net/problem/25682
n, m, k = map(int, input().split())
board = [ list(input()) for _ in range(n)]

bw_board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
# BW체크판을 만들기 위해서...! 
# 수정이 필요한 부분! 기록
for idx, row in enumerate(board):
    for i in range(m):
        if (i + idx) % 2 == 0 and row[i] != 'B':
            bw_board[idx + 1][i + 1] = 1
        elif (i + idx) % 2 != 0 and row[i] != 'W':
            bw_board[idx + 1][i + 1] = 1

# 누적합..
# (x1, y1) ~ (x2, y2) 구간 내의 합이 곧 수정해야할 체스판을 의미함
psum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for r in range(1, n + 1):
    for c in range(1, m + 1):
        psum[r][c] = bw_board[r][c] + psum[r-1][c] + psum[r][c-1] - psum[r-1][c-1]


ans = k * k
for top_r in range(1, n + 2 - k):
    for top_c in range(1, m + 2 - k):
        bottom_r, bottom_c = top_r + k - 1, top_c + k - 1 
        bw_cnt = psum[bottom_r][bottom_c]  - psum[top_r-1][bottom_c] - psum[bottom_r][top_c-1] + psum[top_r-1][top_c-1]
        ans = min(ans, bw_cnt, k * k - bw_cnt)
        
print(ans)