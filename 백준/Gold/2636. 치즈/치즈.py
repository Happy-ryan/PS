from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def find_outside_air():
    outside_air = []
    
    dq = deque([])
    
    in_queue = [[False for _ in range(m)] for _ in range(n)]
    for start in [(0, 0)]:
        r, c = start
        dq.append((r, c))
        in_queue[r][c] = True
        outside_air.append((r, c))
        
    while dq:
        cr, cc = dq.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] == 0:
                dq.append((nr, nc))
                in_queue[nr][nc] = True
                outside_air.append((nr, nc))
                
    return outside_air


def simulate():
    outside_air = find_outside_air()
    
    cnt = 0
    for air in outside_air:
        i, j = air
        for k in range(4):
            n_i, n_j = i + dr[k], j + dc[k]
            if in_range(n_i, n_j) and board[n_i][n_j] == 1:
                board[n_i][n_j] = 0
                cnt += 1    
                
    return cnt

t = 0
ans = 0
while True:
    cnt = simulate()
    if cnt == 0:
        break
    t += 1
    ans = cnt
    
print(t)
print(ans)