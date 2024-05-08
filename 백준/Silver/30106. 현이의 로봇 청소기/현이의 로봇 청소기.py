n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque


def solution(n, m, k, board):
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    inf = int(1e18)
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def bfs(r, c):
        
        dq = deque([])
        dq.append((r, c))
        visited[r][c] = True
        
        while dq:
            cr, cc = dq.popleft()
            for dir in range(4):
                nr = cr + dr[dir]
                nc = cc + dc[dir]
                if in_range(nr, nc) and\
                    not visited[nr][nc] and\
                    abs(board[nr][nc] - board[cr][cc]) <= k:        
                    dq.append((nr, nc))
                    visited[nr][nc] = True
                    
    def end_clean():
        for r in range(n):
            for c in range(m):
                if not visited[r][c]:
                    return False
        return True
    
    cnt = 0
    for r in range(n):
        for c in range(m):
            if visited[r][c]:
                continue
            bfs(r, c)
            cnt += 1
            
    return cnt

print(solution(n, m, k, board))