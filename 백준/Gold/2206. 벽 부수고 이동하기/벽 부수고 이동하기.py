n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

from collections import deque
def solution(n, m, board):
    # 왜 bfs? 그래프 상에서 이동거리 최소 찾기
    # 특이점
        # 벽을 부순 것과 안부순 상태를 확인해서 이동!
        # 벽의 상태에 대한 차원이 필요함. > 벽을 부수면 더 빨라질 가능성이 있기 때문

    # 행, 열, 차원
    inf = int(1e18)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    in_queue = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
    dist = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(2)]
        
    def in_range(r, c, k):
        return 0 <= r < n and 0 <= c < m and 0 <= k < 2
    
    def bfs(r, c, k):
        dq = deque([])
        
        # (행, 열, 벽)
        dq.append((r, c, k))
        in_queue[k][r][c] = True
        dist[k][r][c] = 1
        
        while dq:
            cr, cc, ck = dq.popleft()
            for dir in range(4):
                nr = cr + dr[dir]
                nc = cc + dc[dir]
                if in_range(nr, nc, ck) and not in_queue[ck][nr][nc] and board[nr][nc] == '0':
                    dq.append((nr, nc, ck))
                    in_queue[ck][nr][nc] = True
                    dist[ck][nr][nc] = dist[ck][cr][cc] + 1
                
                # (point) 벽 부수기  - 다음 칸에 벽이 있어야함(board[nr][nc] == 1)
                nk = ck + 1
                if in_range(nr, nc, nk) and not in_queue[nk][nr][nc] and board[nr][nc] == '1':
                    dq.append((nr, nc, nk))
                    in_queue[nk][nr][nc] = True
                    dist[nk][nr][nc] = dist[ck][cr][cc] + 1
        
        return dist
    
    
    dist = bfs(0, 0, 0)
    
    ans = inf
    
    for ver in range(2):
        ans = min(dist[ver][n - 1][m - 1], ans)
        
    if ans >= inf:
        return -1
    
    return ans
        
print(solution(n, m, board))