N = int(input())
r1,c1,r2,c2 = map(int,input().split())

in_queue = [[False for col in range(N)] for row in range(N)]
dist = [[0 for col in range(N)] for row in range(N)]

dr = [-2,-2,2,2,0,0]
dc = [-1,1,-1,1,2,-2,2]

from collections import deque
q = deque([(r1,c1)])
in_queue[r1][c1] = True
dist[r1][c1] = 0

def dist_check(r,c):
    return 0 <= r <= N-1 and 0 <= c <= N-1

while q:
    r,c = q.popleft()
    for k in range(6):
        nr = r +dr[k]
        nc = c +dc[k]
        if dist_check(nr,nc) and\
            not in_queue[nr][nc]:
                q.append((nr,nc))
                in_queue[nr][nc] = True
                dist[nr][nc] = dist[r][c]+1

if dist[r2][c2] != 0:
    print(dist[r2][c2])
else: print(-1)