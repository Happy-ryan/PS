from collections import deque


def solution(n, m, board):
    
    visited = [[False for _ in range(m)] for _ in range(n)] 
    
    dr = [-1, 1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, -1, 1, 1, -1, 1, -1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def bfs(r, c):
        
        dq = deque([])
        dq.append((r, c))
        cnt = 1
        visited[r][c] = True
        
        while dq:
            cr, cc = dq.popleft()
            for k in range(8):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == '@':
                    dq.append((nr, nc))
                    visited[nr][nc] = True
                    cnt += 1
            
        return cnt
    
    cnts = []
    for r in range(n):
        for c in range(m):
            if visited[r][c] or board[r][c] == '*':
                continue
            cnt = bfs(r, c)
            cnts.append(cnt)
            
    return len(cnts)
                
    
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    board = [list(input()) for _ in range(n)]
    print(solution(n, m, board))