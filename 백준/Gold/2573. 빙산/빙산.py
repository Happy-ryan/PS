n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def solution(n, m, board):
    
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m

    # ice 그룹 수 및 좌표 -> 나머지 좌표가 waters가 된다.
    # 따라서 ices를 구하는게 더 합리적.
    def find_ice():
        ices = []
        
        in_queue = [[False for _ in range(m)] for _ in range(n)]
        
        def bfs(r, c):
            ice = []
            
            dq = deque([])
            dq.append((r, c))
            ice.append((r, c))
            in_queue[r][c] = True
            
            while dq:
                cr, cc = dq.popleft()
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] != 0:
                        dq.append((nr, nc))
                        ice.append((nr, nc))
                        in_queue[nr][nc] = True
                
            return ice
        
        cnt = 0
        for r in range(n):
            for c in range(m):
                if board[r][c] == 0 or in_queue[r][c]:
                    continue
                ice = bfs(r, c)
                cnt += 1
                ices.extend(ice)
                
        return ices, cnt
    
    # water의 좌표는 사실 필요하지 않음. 얼음의 좌표에서 4방향을 보면 되기 때문에.
    def event(ices):
        event_board = [[0 for _ in range(m)] for _ in range(n)]
        
        for r, c in ices:
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr, nc) and board[nr][nc] == 0:
                    event_board[r][c] -= 1
        
        for r in range(n):
            for c in range(m):
                if board[r][c] > 0:
                    board[r][c] += event_board[r][c]
                    board[r][c] = max(0, board[r][c])
                
    
    t = 0
    while True:
        ices, cnt = find_ice()
        # print(f"녹기 전 t: {t}")
        # for row in board:
        #     print(row)
        # print("=======")
        if cnt == 0:
            return 0

        if cnt >= 2:
            return t
        
        event(ices)
        t += 1   
        # print(f"녹은 후t: {t}")
        # for row in board:
        #     print(row)
        # print("=======")

print(solution(n, m, board))