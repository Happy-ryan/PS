from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

def solution(n, m, board):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 시작점(0, 0) ~ 도착점(n - 1, m - 1)
    # 최단거리 
    # 부서진 벽인지 아닌지 체크하는 차원 필요 - 벽이 부서지냐 안부서지냐
    inf = int(1e18)
    # 열 / 행 / 벽
    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
    dist = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(2)]
    
    def in_range(k, r, c):
        return 0 <= k < 2 and 0 <= r < n and 0 <= c < m
    
    def bfs():
        
        dq = deque([])
        # (벽, 행, 열)
        dq.append((0, 0, 0))
        visited[0][0][0] = True
        dist[0][0][0] = 1
        
        while dq:
            ck, cr, cc = dq.popleft()
            for dir in range(4):
                nr = cr + dr[dir]
                nc = cc + dc[dir]
                # 벽 없을 때
                if in_range(ck, nr, nc) and not visited[ck][nr][nc] and board[nr][nc] == 0:
                    dq.append((ck, nr, nc))
                    visited[ck][nr][nc] = True
                    dist[ck][nr][nc] = dist[ck][cr][cc] + 1
                    
                # 벽 있을 때 / 벽은 1이다.
                nk = ck + 1
                if in_range(nk, nr, nc) and not visited[nk][nr][nc] and board[nr][nc] == 1:
                    dq.append((nk, nr, nc))
                    visited[nk][nr][nc] = True
                    dist[nk][nr][nc] = dist[ck][cr][cc] + 1
                    
    bfs()  
    
    ans = inf
    for i in range(2):
        ans = min(ans, dist[i][-1][-1])

    if ans >= inf:
        ans = -1
        
    return ans            
    
print(solution(n, m, board))