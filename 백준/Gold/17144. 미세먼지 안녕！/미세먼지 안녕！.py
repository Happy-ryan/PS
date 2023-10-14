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
def aircleaner_objs(up_r, down_r):
    ups = deque([])
    for col in range(C):
        ups.append(result_board[up_r][col])
    for row in range(up_r - 1, -1, -1):
        ups.append(result_board[row][-1])
    for col in range(C - 2, -1, -1):
        ups.append(result_board[0][col])
    for row in range(1, up_r):
        ups.append(result_board[row][0])
    
    downs = deque([])
    for col in range(C):
        downs.append(result_board[down_r][col])
    for row in range(down_r + 1, R):
        downs.append(result_board[row][-1])
    for col in range(C - 2, -1, -1):
        downs.append(result_board[R - 1][col])
    for row in range(R - 2, down_r, -1):
        downs.append(result_board[row][0])
        
    return ups, downs

def aircleaner_simulate(ups, downs):
    ups[0] = 0
    ups.pop()
    ups.appendleft(-1)
    
    downs[0] = 0
    downs.pop()
    downs.appendleft(-1)
    
    return ups, downs

def final_simulate(up_r, down_r, ups, downs):
    i = 0
    for col in range(C):
        result_board[up_r][col] = ups[i]
        i += 1
    for row in range(up_r - 1, -1, -1):
        result_board[row][-1] = ups[i]
        i += 1
    for col in range(C - 2, -1, -1):
        result_board[0][col] = ups[i]
        i += 1
    for row in range(1, up_r):
        result_board[row][0] = ups[i]
        i += 1
    i = 0
    for col in range(C):
        result_board[down_r][col] = downs[i]
        i += 1
    for row in range(down_r + 1, R):
        result_board[row][-1] = downs[i]
        i += 1
    for col in range(C - 2, -1, -1):
        result_board[R - 1][col] = downs[i]
        i += 1
    for row in range(R - 2, down_r, -1):
        result_board[row][0] = downs[i]
        i += 1
    return result_board

# 공기 청정기 위치 추출
up_r, down_r = find(board)
for _ in range(T):
    result_board = diffusion_simulate()
    # 공기청정기 대상 행, 열 추출
    ups, downs = aircleaner_objs(up_r, down_r)
    # 공기청정기 작동 후 공기청정기 대상 행, 열 변화 상태
    ups, downs = aircleaner_simulate(ups, downs)
    # 공기청정기 작동 후 변화 상태 board에 반영
    result_board = final_simulate(up_r, down_r, ups, downs)
    # 기존 board를 대체해야하므로 deepcopy로 배열 복사
    board = deepcopy(result_board)
    
sum_val = 0
for row in result_board:
    sum_val += sum(row)
# 공기청정기 -1이 두 번 더해짐. 상쇄해야함.
sum_val += 2

print(sum_val)
