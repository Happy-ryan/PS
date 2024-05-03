n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def solution(n, m, board):
    # 0. 빙하의 덩어리 개수 판단
    # 0-1. 빙하의 덩어리 1개 > 1 진행
    # 0-2. 빙하의 덩어리 2개 이상 > 종료
    # 1. 물들이 존재하는 좌표들 찾기
    # 2. 빙하 녹이기
    # 빙하 덩어리와 물들의 좌표를 찾는 방법 > bfs / dfs
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    
    def find_water():
        # 찾을 때마다 갱신
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        water_grid = []
        
        def bfs(r, c):
            dq = deque([])
            
            dq.append((r, c))
            visited[r][c] = True
            water_grid.append((r, c))
            
            while dq:
                cr, cc = dq.popleft()
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    if in_range(nr,nc) and board[nr][nc] == 0 and not visited[nr][nc]:
                        dq.append((nr, nc))
                        visited[nr][nc] = True
                        water_grid.append((nr, nc))
                
        for r in range(n):
            for c in range(m):
                if visited[r][c] or board[r][c] != 0:
                    continue
                bfs(r, c)
        
        return water_grid
            
    # 녹일 때 주의점은 한 방에 녹여야한다!
    # 찔끔찔끔 녹이면 높이가 0이 되는 지점에서 문제가 발생하게 된다!
    def melting(ices_gird):
        melting_board = [[0 for _ in range(m)] for _ in range(n)]
        
        for r, c in ices_gird:
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr, nc) and board[nr][nc] == 0:
                    melting_board[r][c] -= 1
                    
        for r in range(n):
            for c in range(m):
                # 0이 한계
                board[r][c] = max(board[r][c] + melting_board[r][c], 0)
        
    
    def find_glacier():
        # 찾을 때마다 갱신
        visited = [[False for _ in range(m)] for _ in range(n)]
        ices = []
        
        def bfs(r, c):
            dq = deque([])
            
            dq.append((r, c))
            visited[r][c] = True
            cnt = 1
            ices.append((r, c))
            
            while dq:
                cr, cc = dq.popleft()
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    if in_range(nr,nc) and board[nr][nc] != 0 and not visited[nr][nc]:
                        dq.append((nr, nc))
                        visited[nr][nc] = True
                        cnt += 1
                        ices.append((nr, nc))
            return cnt
        
        
        cnts = []        
        for r in range(n):
            for c in range(m):
                if visited[r][c] or board[r][c] == 0:
                    continue
                cnt = bfs(r, c)
                cnts.append(cnt)
        
        return len(cnts), ices
    

    
    t = 0
    while True:
        cnt, ices = find_glacier()
        if cnt >= 2:
            return t
        if cnt == 0:
            return 0
        melting(ices)
        t += 1

print(solution(n, m, board))