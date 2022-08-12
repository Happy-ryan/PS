n = int(input())
x,y = map(int,input().split())
m = int(input())
# 인접행렬 생성
adj =[[] for row in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

# print(adj)

in_queue = [False]*(n+1)
dist = [0]*(n+1)

from collections import deque
q = deque([x])
in_queue[x] = True
# bfs 진입
while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if not in_queue[nxt]:
            in_queue[nxt] = True
            q.append(nxt)
            dist[nxt] = dist[cur] + 1
if dist[y] > 0:
    print(dist[y])
else:
    print(-1)