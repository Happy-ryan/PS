a,b = map(int,input().split())
N,M = map(int,input().split())
adj = [[] for row in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split()) # x > y : x가 y로 변환
    adj[x].append(y)
    adj[y].append(x)

in_queue = [False]*(N+1)
dist = [-1]*(N+1)
from collections import deque

q = deque([a])
in_queue[a] = True
dist[a] = 0
while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if not in_queue[nxt]:
            q.append(nxt)
            in_queue[nxt] = True
            dist[nxt] = dist[cur] + 1

if dist[b] == -1:
    print(-1)
else:
    print(dist[b])