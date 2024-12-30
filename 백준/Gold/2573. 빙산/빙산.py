n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def solution(n, m, board):
    inf = int(1e18)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m 
    
    def find_ice():
        
        in_queue = [[False for _ in range(m)] for _ in range(n)]
        
        def bfs(r, c):
            dq = deque([])
            grid = []
            dq.append((r, c))
            in_queue[r][c] = True
            grid.append((r, c))
            
            while dq:
                cr, cc = dq.popleft()
                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] != 0:
                        dq.append((nr, nc))
                        in_queue[nr][nc] = True
                        grid.append((nr, nc))
            return grid
                        
        ice_groups = []
        for i in range(n):
            for j in range(m):
                if in_queue[i][j] or board[i][j] == 0:
                    continue
                grid = bfs(i, j)
                ice_groups.append(grid)
            
        return ice_groups
    
    def meet_water(ice_groups):
        water_board = [[0 for _ in range(m)] for _ in range(n)]
        
        for ice_group in ice_groups:
            for cr, cc in ice_group:
                cnt = 0
                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    if in_range(nr, nc) and board[nr][nc] == 0:
                        cnt += 1
                        # print("여기")
                water_board[cr][cc] = cnt
        return water_board
    
    def melt(water_board):
        for i in range(n):
            for j in range(m):
                if board[i][j] > 0:
                    board[i][j] = max(0, board[i][j] - water_board[i][j])
                    
    def one_time():
        nonlocal ice_groups
        water_board = meet_water(ice_groups)
        melt(water_board)
        ice_groups = find_ice()
        # 녹은 후 빙하그룹의 수
        return len(ice_groups)
    
    
    time = 0
    ice_groups = find_ice()
    while True:
        time += 1
        ice_group_cnt = one_time()
        if ice_group_cnt >= 2:
            return time
        # 빙하 그룹이 없다는 것은 분리되지 않았다는 것!!
        if ice_group_cnt == 0:
            return 0
    
    
print(solution(n, m, board))