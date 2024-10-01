n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

from collections import deque

def solution(n, m, board):
    
    inf = int(1e18)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    in_queue = [[False for _ in range(m)] for _ in range(n)]
    dist = [[inf for _ in range(m)] for _ in range(n)]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def bfs(r, c):
        
        dq = deque([])
        dq.append((r, c))
        dist[r][c] = 1
        in_queue[r][c] = 0
        
        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr,nc) and not in_queue[nr][nc] and board[nr][nc] == '1':
                    dq.append((nr, nc))
                    dist[nr][nc] = dist[cr][cc] + 1
                    in_queue[nr][nc] = True
                    
        return dist
    
    dist = bfs(0, 0)
    
    return dist[n - 1][m -1]


print(solution(n, m, board))