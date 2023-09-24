from copy import deepcopy

n = int(input())
cmds = input()
# 격자 내 이동 - 동남서북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(r, c):
    return 0 <= r < 50 and 0 <= c < 50

def simulate(cr, cc, cmds):
    # 현재 방향
    dir = 1    
    board[cr][cc] = 1
    for cmd in cmds:
        if cmd == 'R':
            dir = (dir + 1) % 4
        elif cmd == 'L':
            dir = (dir + 3) % 4
        else:
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if in_range(nr, nc):
                cr, cc = nr, nc
                board[cr][cc] = 1
            else:
                return False
    return True

result_board = None  # result_board 초기화
for r in range(50):
    for c in range(50):
        board = [[0 for _ in range(50)] for _ in range(50)]
        if  not simulate(r, c, cmds):
            continue
        result_board = deepcopy(board)  # board를 복사하여 result_board에 저장
        break
    if result_board is not None:
        break

max_r, min_r, max_c, min_c = 0, 50, 0, 50

for r in range(50):
    for c in range(50):
        if board[r][c] == 1:
            max_r = max(max_r, r)
            min_r = min(min_r, r)
            max_c = max(max_c, c)
            min_c = min(min_c, c)

# print(max_r, max_c, min_r, min_c)
for r in range(min_r, max_r + 1):
    for c in range(min_c, max_c + 1):
        if result_board[r][c] == 0:
            print('#', end = '')
        else:
            print('.', end = '')
    print()