n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
from copy import deepcopy

def find_grids(r, c, n, m):
    # (r, c)는 좌측 상단을 의미한다.
    grids = deque([])
    for col in range(c, c + m):
        grids.append((r, col))
    for row in range(r + 1, r + n):
        grids.append((row, c + m - 1))
        
    for col in range(c + m - 2, c - 1, -1):
        grids.append((r + n - 1, col))
    for row in range(r + n - 2, r, -1):
        grids.append((row, c))

    return grids

def rotate(girds, r):
    r %= len(girds)
    
    girds.rotate(-r)
    
    return girds

def solution(n, m, r, board):
    
    new_board = [[0 for _ in range(m)] for _ in range(n)]
    
    for k in range(min(n, m) // 2):
        grids = find_grids(0 + k, 0 + k, n - 2 * k, m - 2 * k)
        rotate_grids = rotate(deepcopy(grids), r)
        for i in range(len(grids)):
            new_board[grids[i][0]][grids[i][1]] = board[rotate_grids[i][0]][rotate_grids[i][1]]
    
    for row in new_board:
        print(*row)


solution(n, m, r, board)
