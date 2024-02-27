from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]

def solution(n, board):
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    in_queue = [[False for _ in range(n)] for _ in range(n)]
    dq = deque([])
    
    def in_range(r, c):
        return  0 <= r < n and 0 <= c < n
    
    def bfs(r, c):
        cnt = 0
        
        dq.append((r, c))
        in_queue[r][c] = True
        cnt += 1
        
        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] == '1':
                    dq.append((nr, nc))
                    in_queue[nr][nc] = True
                    cnt += 1
                    
        return cnt
                    
    cnts = []
    for r in range(n):
        for c in range(n):
            if in_queue[r][c] or board[r][c] == '0':
                continue
            cnt = bfs(r, c)
            cnts.append(cnt)
            
    cnts.sort()
    print(len(cnts))
    for cnt in cnts:
        print(cnt)

solution(n, board)