n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

from collections import deque

def solution(n, m, board):
    
    inf = int(1e18)
    # 최단경로 > bfs(거리 1단위) / 다익스트라(거리 2이상 단위) > bfs
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    in_queue = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
    dist = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(2)]
    
    def in_range(k, r, c):
        return 0 <= r < n and 0 <= c < m and 0 <= k < 2
    
    def bfs(k, r, c):
        dq = deque([])
        dq.append((k, r, c))
        in_queue[k][r][c] = True
        dist[k][r][c] = 1
        
        while dq:
            ck, cr, cc = dq.popleft()
            for dir in range(4):
                nr = cr + dr[dir]
                nc = cc + dc[dir]
                if in_range(ck, nr, nc) and not in_queue[ck][nr][nc] and board[nr][nc] == '0':
                    dq.append((ck, nr, nc))
                    in_queue[ck][nr][nc] = True
                    dist[ck][nr][nc] = dist[ck][cr][cc] + 1
                    
            # 벽 부딪힘
            nk = ck + 1
            for dir in range(4):
                nr = cr + dr[dir]
                nc = cc + dc[dir]
                # 벽이어야함!
                if in_range(nk, nr, nc) and not in_queue[nk][nr][nc] and board[nr][nc] == '1':
                    dq.append((nk, nr, nc))
                    in_queue[nk][nr][nc] = True
                    dist[nk][nr][nc] = dist[ck][cr][cc] + 1
                    
    bfs(0, 0, 0)
    
    ans = inf
    for i in range(2):
        ans = min(ans, dist[i][n - 1][m - 1])
        
    if ans >= inf:
        return -1
    return ans

print(solution(n, m, board))