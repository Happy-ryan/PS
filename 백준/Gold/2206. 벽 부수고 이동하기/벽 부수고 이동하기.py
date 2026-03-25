n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

from collections import deque

def solution(n, m , board):
    inf = int(1e18)
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 벽 부수는 차원 추가 (0 : 정상 / 1 : 부숨)
    in_queue = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
    dist = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(2)]
    
    def in_range(k, r, c):
        return 0 <= r < n and 0 <= c < m and 0 <= k <= 1
    
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
                if in_range(ck, nr, nc) and\
                    not in_queue[ck][nr][nc] and\
                        board[nr][nc] == '0': # 벽이 아닐 때 이동 가능
                            dq.append((ck, nr, nc))
                            in_queue[ck][nr][nc] = True
                            dist[ck][nr][nc] = dist[ck][cr][cc] + 1
            # 벽 부수는 차원
            nk = ck + 1
            for dir in range(4):
                nr = cr + dr[dir]
                nc = cc + dc[dir]
                if in_range(nk, nr, nc) and\
                    not in_queue[nk][nr][nc] and\
                        board[nr][nc] == '1': # 벽일 때 박살내고 이동가능
                            dq.append((nk, nr, nc))
                            in_queue[nk][nr][nc] = True
                            dist[nk][nr][nc] = dist[ck][cr][cc] + 1
                            
    
    bfs(0, 0, 0)
        
    min_dist = min(dist[0][n - 1][m - 1], dist[1][n - 1][m - 1])
    
    answer = -1 if min_dist >= inf else min_dist
    
    return answer
            
print(solution(n, m, board))