from collections import deque
import sys, pprint

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [list(map(int, input().split())) for row in range(N)]
res = [[0 for col in range(M)] for row in range(N)]

inf = int(1e8)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find(adj, N, M):
    for r in range(N):
        for c in range(M):
            if adj[r][c] == 2:
                return (r, c)

x = find(adj, N, M)[0]
y = find(adj, N, M)[1]

def bfs(r, c):  

    in_queue = [[False for col in range(M)] for row in range(N)]
    dist = [[inf for col in range(M)] for row in range(N)]
    
    def check(r, c):
        return 0<= r < N and 0<= c < M and in_queue[r][c] == False
    

    q = deque([])
    q.append((r,c))
    in_queue[r][c] = True
    dist[r][c] = 0

    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if check(nr, nc) and adj[nr][nc] == 1:
                q.append((nr, nc))
                in_queue[nr][nc] = True
                dist[nr][nc] = dist[cr][cc] + 1

    for r in range(N):
        for c in range(M):
            if adj[r][c] == 0:
                dist[r][c] = 0
            else:
                if dist[r][c] >= inf:
                    dist[r][c] = -1

    return dist
    

for row in bfs(x, y):
    print(*row)