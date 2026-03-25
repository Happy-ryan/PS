from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

def solution(n, m, board):
    # (i, j)에 도달한적있냐?
    in_queue = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    # dist[i][j][k] = 시작점에서 k번 만큼 벽을 부수고 (i, j)까지의 최단거리
    # 최대 1번 가능! k = 0 or 1 ..2가 된다!
    # dist[n][m]
    inf = int(1e9)
    dist = [[[inf for _ in range(2)] for _ in range(m)] for _ in range(n)]
    
    def in_range(r, c, k):
        return 0 <= r < n and 0 <= c < m and 0 <= k < 2
    
    def bfs():
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        dq = deque([])
        for r, c, k in [(0, 0, 0)]:
            dq.append((r, c, k))
            in_queue[r][c][k] = True
            dist[r][c][k] = 1
            
        while dq:
            cr, cc, ck = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc, ck) and not in_queue[nr][nc][ck] and board[nr][nc] == 0:
                    dq.append((nr, nc, ck))
                    in_queue[nr][nc][ck] = True
                    dist[nr][nc][ck] = dist[cr][cc][ck] + 1
                
                nk = ck + 1
                if in_range(nr, nc, nk) and not in_queue[nr][nc][nk] and board[nr][nc] == 1:
                    dq.append((nr, nc, nk))
                    in_queue[nr][nc][nk] = True
                    dist[nr][nc][nk] = dist[cr][cc][ck] + 1
                
    bfs()
    min_ans = inf
    for k in range(2):
        min_ans = min(min_ans, dist[n - 1][m - 1][k])
        
    if min_ans >= inf:
        min_ans = -1
        
    return min_ans

print(solution(n, m, board))