n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

from collections import deque

def solution(n, m, board):
    
    inf = int(1e18)
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c, d):
        return 0 <= r < n and 0 <= c < m and 0 <= d < 2
    
    queue = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
    dist = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(2)]
    
    def bfs(r, c, d):
        dq = deque([])
        
        dq.append((r, c, d))
        queue[d][r][c] = True
        dist[d][r][c] = 1
        
        while dq:
            cr, cc, cd = dq.popleft()
            
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k] 
                if in_range(nr, nc, cd) and\
                    board[nr][nc] == 0 and\
                    not queue[cd][nr][nc]:
                        
                        dq.append((nr, nc, cd))
                        queue[cd][nr][nc] = True
                        dist[cd][nr][nc] = dist[cd][cr][cc] + 1
                        
            # 1은 벽 뚫은 세계관
            nd = cd + 1 # cd = 0

            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k] 
                if in_range(nr, nc, nd) and\
                    board[nr][nc] == 1 and\
                    not queue[nd][nr][nc]:
                        
                        dq.append((nr, nc, nd))
                        queue[nd][nr][nc] = True
                        dist[nd][nr][nc] = dist[cd][cr][cc] + 1 # 벽이 뚫리지 않은 세계관에서 벽이 뚫린거니까 cd에서 nd로 처리
                        
    bfs(0, 0, 0)

    ans = inf
    for i in range(2):
        ans = min(ans, dist[i][n - 1][m - 1])
        
    if ans >= inf:
        return -1
    return ans

print(solution(n, m, board))