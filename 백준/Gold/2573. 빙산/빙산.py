n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def solution(n, m, board):
    
    # 빙하 / 물 <- 빙하가 주변의 물에 영향을 받는다는 것..
    # 한번에 영향을 받아 동시에 녹아야함..
    # 따라서 각 빙하에 접한 물의 수를 알아야함.
    
    # point1. bfs 을 통해서 빙하 그룹 수 파악
    # point2. 빙하 위치 파악과 물의 영향도 파악
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def find_ice():
        ices = []
        for i in range(n):
            for j in range(m):
                if board[i][j] != 0:
                    ices.append((i, j))
        return ices
    
    def bfs(ices):
        
        queue = [[False for _ in range(m)] for _ in range(n)]
        
        cnts = []
        
        for ice in ices:
            r, c = ice
            
            if queue[r][c] or board[r][c] == 0: # 못도는거 체크
                continue
            
            dq = deque([])
            
            dq.append((r, c))
            queue[r][c] = True
            cnt = 1
            
            while dq:
                cr, cc = dq.popleft()
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    if  in_range(nr, nc) and\
                        board[nr][nc] != 0 and\
                        not queue[nr][nc]:
                            dq.append((nr, nc))
                            queue[nr][nc] = True
                            cnt += 1
            cnts.append(cnt)
            
        return len(cnts) # cnts 1개 - 정상 / 2개 - 나눠짐 / 0개 - 다 녹음
        

    def water_effect(ices):
        waters = [[0 for _ in range(m)] for _ in range(n)]
        
        for ice in ices:
            cr, cc = ice
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and board[nr][nc] == 0:
                    waters[cr][cc] -= 1
                    
        for i in range(n):
            for j in range(m):
                board[i][j] = max(0, board[i][j] + waters[i][j])
                
    
    t = 0
    while True:
        ices = find_ice()
        # print("영향 받기 전")
        # for row in board:
        #     print(row)
        water_effect(ices) 
        # print("영향 받기 후")
        # for row in board:
        #     print(row)
        t += 1 
        cnt = bfs(ices)
        # print("그룹 수", cnt)
        if cnt == 0:
            return 0
        if cnt >= 2:
            return t

print(solution(n, m, board))