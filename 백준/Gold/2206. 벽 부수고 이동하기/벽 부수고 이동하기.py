n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(n, m , board):
    # 벽이 최대 1개 부술 수 있다.
    # 최대 벽이 선택될 수 있는 경우의 수는 n * m + bfs > 시간초과
    # 부서진 벽에 대한 정보를 기록해야한다! > 차원을 하나 추가해야한다!!
    # 벽을 부술 수도 있고 안 부술 수도 있다. 즉,
    in_queue = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    inf = int(1e9)
    # dist[i][j][j] (0, 0) ~ (i, j)까지 벽을 k번 부쉈을 때의 최단거리
    dist = [[[inf for _ in range(2)] for _ in range(m)] for _ in range(n)]
    
    def in_range(r, c, k):
        return 0 <= r < n and  0 <= c < m and 0 <= k < 2
    
    def bfs():
        dq = deque([])
        # r, c, k(벽 유무)
        dq.append((0, 0, 0))
        in_queue[0][0][0] = True
        dist[0][0][0] = 1
    
        while dq:
            cr, cc, ck = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                # 벽이 아닐 때 지나가겠다.
                # board -> 0일 때!
                if in_range(nr, nc, ck) and not in_queue[nr][nc][ck] and board[nr][nc] == 0:
                    dq.append((nr, nc, ck))
                    in_queue[nr][nc][ck] = True
                    dist[nr][nc][ck] = dist[cr][cc][ck] + 1
                
                # 벽을 부수겠다!
                # board에서 1을 선택해야함!
                nk = ck + 1
                if in_range(nr, nc, nk) and not in_queue[nr][nc][nk] and board[nr][nc] == 1:
                    dq.append((nr, nc, nk))
                    in_queue[nr][nc][nk] = True
                    # 그 전에서 와야함으로 nk <- ck + 1이 맞다.
                    dist[nr][nc][nk] = dist[cr][cc][ck] + 1
                    
    bfs()
    min_ans = inf
    # k = 0 벽이 안부셔진 경우
    # k = 1 일때는 벽이 부서진 경우
    for k in range(2):
        min_ans = min(min_ans, dist[n - 1][m - 1][k])
        
    # 불가능한 경우
    if min_ans >= inf:
        min_ans = -1
        
    return min_ans

print(solution(n, m, board))