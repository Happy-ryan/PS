import sys
from collections import deque

input = sys.stdin.readline
L,W = map(int,input().split())
graph = [ list(input()) for row in range(L)]


def check(r,c):
    return 0<= r < L and 0<= c < W and graph[r][c] == 'L'

def bfs(r,c):
    in_queue = [[False for col in range(W)] for row in range(L) ]
    dist = [[0 for col in range(W)] for row in range(L)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    q = deque([])
    q.append((r,c))
    in_queue[r][c] = True

    while q:
        cr,cc = q.popleft()

        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if check(nr,nc) and\
                not in_queue[nr][nc]:
                q.append((nr,nc))
                in_queue[nr][nc] = True
                dist[nr][nc] = dist[cr][cc] + 1
    ans = 0
    for i in range(L):
        ans = max(ans,max(dist[i]))
    return ans

res = 0
for y in range(L):
    for x in range(W):
        if graph[y][x] == 'W':
            continue
        res = max(res,bfs(y,x))
    
print(res)