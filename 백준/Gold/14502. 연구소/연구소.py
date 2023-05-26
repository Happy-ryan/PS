# https://www.acmicpc.net/problem/14502
from collections import deque
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for row in range(n)]


def candidate_wall(n, m, board):
    walls = []
    for r in range(n):
        for c in range(m):
            if board[r][c] == 0:
                walls.append((r, c))
    return walls


def bfs(n, m , board):
    in_queue = [[False for col in range(m)] for row in range(n)]
    virus = [[0 for col in range(m)] for row in range(n)]
        
    def check(r, c):
        return 0<= r < n and 0<= c < m and not in_queue[r][c] and\
            board[r][c] == 0
            
            
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    q = deque([])
    
    cnt_wall = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] == 2:
                q.append((r, c))
                in_queue[r][c] = True
                # virus[r][c] = 0
            elif board[r][c] == 1:
                cnt_wall += 1

    cnt_virus = 0 
    while q:
        cr, cc = q.popleft()
        cnt_virus += 1
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if check(nr, nc):
                board[nr][nc] = 2 # 감염 0 > 2
                in_queue[nr][nc] = True
                q.append((nr, nc)) 
                
    ans = n * m - cnt_wall - cnt_virus
    
    return ans
    
# wall 이 아마 계속 채워지는 것 같음.
def solution(n, m, board):
    ans = 0
    walls = candidate_wall(n, m , board)
    for wall_1, wall_2, wall_3 in combinations(walls, 3):
        original = deepcopy(board)
        original[wall_1[0]][wall_1[1]] = 1
        original[wall_2[0]][wall_2[1]] = 1
        original[wall_3[0]][wall_3[1]] = 1
        ans = max(ans, bfs(n, m, original))
    return ans
print(solution(n, m, board))