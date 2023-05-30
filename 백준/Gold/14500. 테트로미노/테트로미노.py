# https://www.acmicpc.net/problem/14500


def check(r, c, n, m):
    return 0<= r < n and 0<= c < m
# ㅁㅁ
# ㅁㅁ
def one(n, m, board):
    sum_val = 0
    for r in range(n - 1):
        for c in range(m - 1):
            sum_val = max(sum_val, board[r][c] + board[r+1][c+1] + board[r][c+1] + board[r+1][c])
    return sum_val
# ㅁㅁㅁㅁ 회전
def two_v1(n, m, board):
    sum_val = 0
    for c in range(m):
        for r in range(n - 3):
            sum_val = max(sum_val, board[r][c] + board[r+1][c] + board[r+2][c] + board[r+3][c])
    return sum_val

# ㅁㅁㅁㅁ 
def two_v2(n, m, board):
    sum_val = 0
    for r in range(n):
        for c in range(m - 3):
            sum_val = max(sum_val, board[r][c] + board[r][c+1] + board[r][c+2] + board[r][c+3])
    return sum_val

# ㅜ 모양
def three_v1(n, m, board):
    sum_val = 0
    for r in range(n - 1):
        for c in range(m - 2):
            sum_val = max(sum_val, board[r][c] + board[r][c+1] + board[r][c+2]+board[r+1][c+1])
    return sum_val

# ㅏ , ㅓ 모양 board모양만 반대로!
def three_v2(n, m, board):
    sum_val = 0
    for r in range(n - 2):
        for c in range(m - 1):
            sum_val = max(sum_val, board[r][c] + board[r+1][c] + board[r+1][c+1] + board[r+2][c])
    return sum_val

# ㅗ 모양
def three_v3(n, m, board):
    sum_val = 0
    for r in range(1, n):
        for c in range(m - 2):
            sum_val = max(sum_val, board[r][c] + board[r][c+1] + board[r-1][c+1] + board[r][c+2])
    return sum_val

# ㅓ 모양, ㅏ 모양 반대 맵 넣기
def three_v3(n, m, board):
    sum_val = 0
    for r in range(1, n):
        for c in range(m - 2):
            sum_val = max(sum_val, board[r][c] + board[r][c+1] + board[r-1][c+1] + board[r][c+2])
    return sum_val
            
# ㄴ 모양, 반대 ㄴ 모양 
# |
# | _
def four_v1(n, m, board):
    sum_val = 0
    for r in range(n - 2):
        for c in range(m - 1):
            sum_val = max(sum_val, 
                        board[r][c] + board[r+1][c] + board[r+2][c] + board[r+2][c+1],
                        board[r][c] + board[r][c+1] + board[r+1][c+1] +
                        board[r+2][c+1])
    return sum_val
# | _ _ 모양, 반대모양까지
def four_v2(n, m, board):
    sum_val = 0
    for r in range(n - 1):
        for c in range(m - 2):
            sum_val = max(sum_val, 
                        board[r][c] + board[r+1][c] + board[r+1][c+1] + board[r+1][c+2],
                        board[r][c] + board[r][c+1] + board[r][c+2] +
                        board[r+1][c+2])
    return sum_val

# 세워짐 ㄱㄴ, 반대맵 넣기
def five_v1(n, m, board):
    sum_val = 0
    for r in range(n - 2):
        for c in range(m - 1):
            sum_val = max(sum_val, board[r][c]+board[r+1][c]+board[r+1][c+1]+board[r+2][c+1])
    return sum_val

# 누워짐 ㄱㄴ, 반대맵 넣기
def five_v2(n, m, board):
    sum_val = 0
    for r in range(n - 1):
        for c in range(m - 2):
            sum_val = max(sum_val, board[r][c] + board[r][c+1] + board[r+1][c+1] + board[r+1][c+2])
    return sum_val

from pprint import pprint
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]  
reverse_board = [row[::-1] for row in board]
# 1
one_val = one(n, m, board) 
# 2
two_v1_val = two_v1(n, m, board) 
two_v2_val = two_v2(n, m, board)
# 4
three_v1_val = three_v1(n, m, board)
three_v3_val = three_v3(n, m, board)
three_v2_1_val = three_v2(n, m , board)
three_v2_2_val = three_v2(n, m , reverse_board)
# 8
four_v1_1_val = four_v1(n, m, board)
four_v1_2_val = four_v1(n, m, reverse_board)
four_v2_1_val = four_v2(n, m, board)
four_v2_2_val = four_v2(n, m, reverse_board)
# 4
five_v1_1_val = five_v1(n, m , board)
five_v1_2_val = five_v1(n, m , reverse_board)
five_v2_1_val = five_v2(n, m , board)
five_v2_2_val = five_v2(n, m , reverse_board)

print(max(one_val,
    two_v1_val,
    two_v2_val,
    three_v1_val,
    three_v2_1_val,
    three_v2_2_val,
    three_v3_val,
    four_v1_1_val,
    four_v1_2_val,
    four_v2_1_val,
    four_v2_2_val,
    five_v2_1_val,
    five_v2_2_val,
    five_v1_1_val,
    five_v1_2_val,))
