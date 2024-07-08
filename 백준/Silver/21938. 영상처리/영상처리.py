from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

def solution(n, m, board, t):
    
    new_board = [[0 for _ in range(m)] for _ in range(n)]
        
    for i in range(n):
        for j in range(0, 3 * m,  3):
            sum_val = (board[i][j] + board[i][j + 1] + board[i][j + 2])
            
            if sum_val >= 3 * t:
                new_board[i][j // 3] = 255
            else:
                new_board[i][j // 3] = 0
                
    visited = [[False for _ in range(m)] for _ in range(n)] 
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def bfs(r, c):
        
        dq = deque([])
        dq.append((r, c))
        cnt = 1
        visited[r][c] = True
        
        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not visited[nr][nc] and new_board[nr][nc] == 255:
                    dq.append((nr, nc))
                    visited[nr][nc] = True
                    cnt += 1
            
        return cnt
    
    cnts = []
    for r in range(n):
        for c in range(m):
            if visited[r][c] or new_board[r][c] == 0:
                continue
            cnt = bfs(r, c)
            cnts.append(cnt)
            
    return len(cnts)
            
        
print(solution(n, m, board, t))