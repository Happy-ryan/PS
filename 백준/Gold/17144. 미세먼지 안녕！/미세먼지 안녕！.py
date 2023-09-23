from collections import deque
from copy import deepcopy

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def find(board):
    rs = []
    for r in range(R):
        if board[r][0] == -1:
            rs.append(r)
        
    return min(rs), max(rs)

def in_range(r, c):
    return 0 <= r < R and 0 <= c < C and board[r][c] != -1

# 1초 - 확산
def diffusion_simulate():
    diffusion_board = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] != 0 and board[r][c] != -1:
                diffuse_val = board[r][c] // 5
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if in_range(nr, nc):
                        board[r][c] -= diffuse_val
                        diffusion_board[nr][nc] += diffuse_val
                        
    result_board = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == -1:
                result_board[r][c] = -1
            else:
                result_board[r][c] = diffusion_board[r][c] + board[r][c]
                
    return result_board

# 공기청정기 대상 행, 열 추출
def aircleaner_objs(board, up_r, down_r):
    ups = deque([])
    for col in range(C):
        ups.append(board[up_r][col])
    for row in range(up_r - 1, -1, -1):
        ups.append(board[row][-1])
    for col in range(C - 2, -1, -1):
        ups.append(board[0][col])
    for row in range(1, up_r):
        ups.append(board[row][0])
    
    downs = deque([])
    for col in range(C):
        downs.append(board[down_r][col])
    for row in range(down_r + 1, R):
        downs.append(board[row][-1])
    for col in range(C - 2, -1, -1):
        downs.append(board[R - 1][col])
    for row in range(R - 2, down_r, -1):
        downs.append(board[row][0])
        
    return ups, downs

def aircleaner_simulate(ups, downs):
    ups[0] = 0
    ups.pop()
    ups.appendleft(-1)
    
    downs[0] = 0
    downs.pop()
    downs.appendleft(-1)
    
    return ups, downs

def final_simulate(board, up_r, down_r, ups, downs):
    i = 0
    for col in range(C):
        board[up_r][col] = ups[i]
        i += 1
    for row in range(up_r - 1, -1, -1):
        board[row][-1] = ups[i]
        i += 1
    for col in range(C - 2, -1, -1):
        board[0][col] = ups[i]
        i += 1
    for row in range(1, up_r):
        board[row][0] = ups[i]
        i += 1
    i = 0
    for col in range(C):
        board[down_r][col] = downs[i]
        i += 1
    for row in range(down_r + 1, R):
        board[row][-1] = downs[i]
        i += 1
    for col in range(C - 2, -1, -1):
        board[R - 1][col] = downs[i]
        i += 1
    for row in range(R - 2, down_r, -1):
        board[row][0] = downs[i]
        i += 1
    return board

for _ in range(T):
    result_board = diffusion_simulate()
    up_r, down_r = find(board)
    ups = aircleaner_objs(result_board, up_r, down_r)[0]
    downs = aircleaner_objs(result_board, up_r, down_r)[1]
    ups, downs = aircleaner_simulate(ups, downs)
    result_board = final_simulate(result_board, up_r, down_r, ups, downs)
    # 기존 board를 대체해야하므로 deepcopy로 배열 복사
    board = deepcopy(result_board)
    
sum_val = 0
for row in result_board:
    sum_val += sum(row)

sum_val += 2

print(sum_val)