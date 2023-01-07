# 2차원 BFS/DFS - BFS풀이
from collections import deque

def solution(maps):
    
    answer, inf = 0, int(1e8)
    R, C = len(maps), len(maps[0])
    dist = [[inf for col in range(C)] for row in range(R)]
    in_queue = [[False for col in range(C)] for row in range(R)]
    
    dr = [-1, 1, 0 ,0]
    dc = [0, 0, -1, 1]
    
    def check(r, c):
        return 0<= r < R and 0<= c < C and in_queue[r][c] == False
    
    def bfs(maps, r, c):
        q = deque([(r, c)])
        in_queue[r][c] = True
        dist[r][c] = 0
        
        while q:
            cr, cc = q.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if check(nr, nc) and maps[nr][nc] == 1:
                    q.append((nr, nc))
                    in_queue[nr][nc] = True
                    dist[nr][nc] = dist[cr][cc] + 1
                    
        return dist[R - 1][C - 1]
    
    answer = bfs(maps, 0, 0) 
    if answer >= inf:
        return -1
    else:
        return answer + 1