
from collections import deque

R, C = map(int, input().split())
schools = [list(input()) for row in range(R)]

inf = int(1e8)

in_queue = [[False for col in range(C)] for row in range(R)]
dist = [[inf for col in range(C)] for row in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1 ,1]

def find(R, C, find):
    for r in range(R):
        for c in range(C):
            if schools[r][c] == find:
                return (r, c)
    
def check(r, c):
    return 0<= r < R and 0<= c < C and not in_queue[r][c]

def bfs(r, c):
    q = deque([(r, c)])
    in_queue[r][c] = True
    dist[r][c] = 0

    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if check(nr, nc) and schools[nr][nc] != 'X':
                q.append((nr, nc))
                in_queue[nr][nc] = True
                dist[nr][nc] = dist[cr][cc] + 1
    return dist

bfs(find(R, C, 'I')[0], find(R, C, 'I')[1])

cnt = 0
for r in range(R):
    for c in range(C):
        if schools[r][c] == 'P' and 0 < dist[r][c] < inf:
            cnt += 1
if cnt == 0:
    print('TT')
else:
    print(cnt)