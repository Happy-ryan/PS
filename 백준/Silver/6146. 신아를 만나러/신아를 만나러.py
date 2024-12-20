x, y, n = map(int, input().split())
grids = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def solution(x, y, n, grids):
    base = 502
    max_n = base * 2
    inf = int(1e18)
    
    board = [[0 for _ in range(max_n)] for _ in range(max_n)]
    dist = [[inf for _ in range(max_n)] for _ in range(max_n)]
    in_queue = [[False for _ in range(max_n)] for _ in range(max_n)]
    
    # 시작점 (0, 0) -> (1000, 1000)
    for grid in grids:
        r, c = grid
        board[r + base][c + base] = 1
        in_queue[r + base][c + base] = True
        
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < max_n and 0 <= c < max_n
    
    def bfs(r, c):
        dq = deque([])
        dq.append((r, c))
        dist[r][c] = 0
        in_queue[r][c] = True
        
        while dq:
            r, c = dq.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] == 0:
                    dq.append((nr, nc))
                    dist[nr][nc] = dist[r][c] + 1
                    in_queue[nr][nc] = True

        return dist
    
    dist = bfs(0 + base, 0 + base)
    # for row in dist:
    #     print(row)
    return dist[x + base][y + base]

print(solution(x, y, n, grids))