M,N = map(int,input().split()) # N - row - 세로
adj = [ list(map(int,input().split())) for row in range(N)]

in_queue = [[False for col in range(M)] for row in range(N)]
dist = [[0 for col in range(M)] for row in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def adj_check(r,c):
    return 0<= r < N and 0<= c < M

from collections import deque
# 토마토 문제의 포인트 : 동시에 다양한 지점이 출발점이 된다는 것
# 따라서 각 출발점들을 q에 미리 넣어서 가상의 노드가 있다고 생각하고 q에 넣는 것
# 가상의 노드로(1번) > 각 출발점들을 너비탐색하는 것!!

q = deque([])

for r in range(N):
    for c in range(M):
        if adj[r][c] == 1:
            q.append((r,c)) 
            in_queue[r][c] = True

# 각 출발점들을 너비탐색
while q:
    cr,cc = q.popleft()
    adj[cr][cc] = 1 # 익지 않은 토마토 0 > 익은 토마토 1로 변경
    for k in range(4):
        nr = cr + dr[k]
        nc = cc + dc[k]
        if adj_check(nr,nc) and\
            not in_queue[nr][nc] and\
                adj[nr][nc] != -1:
                q.append((nr,nc))
                in_queue[nr][nc] = True # 방문체크
                dist[nr][nc] = dist[cr][cc] + 1

# print(dist)
# print(adj)
ans = 0
for x in range(N):
    for y in range(M):
        ans = max(ans,dist[x][y])

for i in range(N):
    for j in range(M):
        if adj[i][j] == 0:
            ans = -1

print(ans)