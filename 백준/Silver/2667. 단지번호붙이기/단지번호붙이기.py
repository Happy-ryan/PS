n = int(input())
board = [list(input()) for _ in range(n)]

# bfs
from collections import deque

def solution(n, board):
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    in_queue = [[False for _ in range(n)] for _ in range(n)]
    
    def bfs(r, c):
        dq = deque([])
        
        dq.append((r, c))
        in_queue[r][c] = True
        cnt = 1
        
        while dq:
            cr, cc = dq.popleft()
            for  k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and\
                    not in_queue[nr][nc] and\
                        board[nr][nc] == '1':
                            dq.append((nr, nc))
                            in_queue[nr][nc] = True
                            cnt += 1
        return cnt
        
    cnts = []
    for i in range(n):
        for j in range(n):
            if in_queue[i][j] or board[i][j] == '0':
                continue
            cnt = bfs(i, j)
            cnts.append(cnt)
            
    cnts.sort()
    
    print(len(cnts))
    for c in cnts:
        print(c)
    
solution(n, board)