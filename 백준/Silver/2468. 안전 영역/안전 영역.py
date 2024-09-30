n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def solution(n, board):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    def bfs(r, c, h):
        dq = deque([])
        
        dq.append((r, c))
        in_queue[r][c] = True
        cnt = 1
        
        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and\
                    not in_queue[nr][nc] and\
                    board[nr][nc] > h:
                        
                    dq.append((nr, nc))
                    in_queue[nr][nc] = True
                    cnt += 1
        return cnt
    
    max_area = 0
    for h in range(101):
        cnts = []
        in_queue = [[False for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if board[r][c] <= h or in_queue[r][c]:
                    continue
                cnt = bfs(r, c, h)
                cnts.append(cnt)
        max_area = max(max_area, len(cnts))
        # print(f"높이: {h}, max_area: {max_area}")
    
    return max_area

print(solution(n, board))