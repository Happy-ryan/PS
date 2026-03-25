n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque, defaultdict

def solution(n, m, board):
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c and m
    
    def find_ice(): # 빙하 판단
        
        in_queue = [[False for _ in range(m)] for _ in range(n)]
        
        def bfs(r, c):
            dq = deque([])
            
            dq.append((r, c))
            in_queue[r][c] = True
            ice = [(r, c)]
            
            while dq:
                cr, cc = dq.popleft()
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    if in_range(nr, nc) and\
                        not in_queue[nr][nc] and\
                            board[nr][nc] != 0:
                                dq.append((nr, nc))
                                in_queue[nr][nc] = True
                                ice.append((nr, nc))
            return ice
        
        ices = defaultdict(list)
        cnt = 1
        for i in range(n):
            for j in range(m):
                if in_queue[i][j] or board[i][j] == 0:
                    continue
                ice = bfs(i, j)
                ices[cnt] = ice
                cnt += 1
    
        return ices

    def melt(ices): 
        # ices = find_ice().values()
        check_water = []
        for ice in ices:
            for r, c in ice:
                cnt = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if in_range(nr, nc) and\
                        board[nr][nc] == 0:
                            cnt += 1
                check_water.append(cnt)
        
        # print(ices)
        # print(check_water)
        
        for ice in ices:
            for (r, c), cnt in zip(ice, check_water):
                board[r][c] = max(board[r][c] - cnt, 0)

    
    time = 0
    while True:
        ices = find_ice()   # {
                            #    1 : [(r1, c1)...]
                            #  , 2 : [(r2, c2)..]]
                            # }
                            
        if len(ices.keys()) == 0:
            return 0
        
        if len(ices.keys()) >= 2:
            return time
        
        time += 1
        melt(ices.values())
    

print(solution(n, m, board))