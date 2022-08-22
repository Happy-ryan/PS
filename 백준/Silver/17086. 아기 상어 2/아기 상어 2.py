N,M = map(int,input().split())
adj = [ list(map(int,input().split())) for row in range(N)]
dist = [[0 for col in range(M)] for row in range(N)]
in_queue = [[False for col in range(M)] for row in range(N)]
# print(adj)

dr = [-1,1,0,0,-1,-1,1,1]
dc = [0,0,-1,1,1,-1,1,-1]

def adj_check(r,c):
    return 0<= r < N and 0<= c < M


# 토마토 문제와 유사한 문제 : 출발점이 다양한 경우

from collections import deque
q = deque([])

# 하나의 가상의 상위 노드 생성했다고 가정
for r in range(N):
    for c in range(M):
        if adj[r][c] == 1:
            q.append((r,c))
            in_queue[r][c] = True

# print(q)
while q:
    cr,cc = q.popleft()
    for k in range(8):
        nr = cr + dr[k]
        nc = cc + dc[k]
        if adj_check(nr,nc) and\
            not in_queue[nr][nc] and\
                adj[nr][nc] == 0:
                q.append((nr,nc))
                in_queue[nr][nc] = True
                dist[nr][nc] = dist[cr][cc] + 1

# print(dist)

ans = 0
for y in range(N):
    ans = max(ans,max(dist[y]))

print(ans)