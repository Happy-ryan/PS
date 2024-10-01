t = int(input())

from collections import deque

def solution(l, chess):

    inf = int(1e18)
    dr = [-1, 1, 2, 2, -2, -2, -1, 1]
    dc = [2, 2, -1, 1, -1, 1, -2, -2]
    
    in_queue = [[False for _ in range(l)] for _ in range(l)]
    dist = [[inf for _ in range(l)] for _ in range(l)]
    
    def in_range(r, c):
        return 0 <= r < l and 0 <= c < l
    
    def bfs(r, c):
        
        dq = deque([])
        dq.append((r, c))
        dist[r][c] = 0
        in_queue[r][c] = True
        
        while dq:
            cr, cc = dq.popleft()
            for k in range(8):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not in_queue[nr][nc]:
                    dq.append((nr, nc))
                    # cr, cc 주의! 변수 주의!!
                    dist[nr][nc] = dist[cr][cc] + 1
                    in_queue[nr][nc] = True
                    
        return dist
    
    start_chess = chess[0]
    end_chess = chess[1]
    
    dist = bfs(start_chess[0], start_chess[1])
    
    return dist[end_chess[0]][end_chess[1]]

for _ in range(t):
    l = int(input())
    chess = [list(map(int, input().split())) for _ in range(2)]
    print(solution(l, chess))