from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(n, m , board):
    in_queue = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
    inf = int(1e18)
    # [높이][행][열]
    dist = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(2)]
    
    
    def in_range(r, c, k):
        return 0 <= r < n and 0 <= c < m and 0 <= k < 2
    
    def bfs():
        dq = deque([])
        
        # (r, c, k)
        dq.append((0, 0, 0))
        in_queue[0][0][0] = True
        dist[0][0][0] = 1
        
        while dq:
            cr, cc, ck = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                # 벽을 안부숨!
                if in_range(nr, nc, ck) and not in_queue[ck][nr][nc] and board[nr][nc] == 0:
                    dq.append((nr, nc, ck))
                    in_queue[ck][nr][nc] = True
                    dist[ck][nr][nc] = dist[ck][cr][cc] + 1
                
                # 벽을 부숨! 현재 위치는 보드에서 '1'을 의미함!
                nk = ck + 1
                if in_range(nr, nc, nk) and not in_queue[nk][nr][nc] and board[nr][nc] == 1:
                    dq.append((nr, nc, nk))
                    in_queue[nk][nr][nc] = True
                    dist[nk][nr][nc] = dist[ck][cr][cc] + 1
                    # board[nr][nc] = 0
    
    bfs()
    min_ans = inf
    for x in range(2):
        min_ans = min(min_ans, dist[x][n - 1][m - 1])
        
    if min_ans >= inf:
        min_ans = -1
        
    return min_ans
    
print(solution(n, m, board))