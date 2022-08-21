N,M = map(int,input().split())
adj = [[] for row in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
# 1-base
in_queue = [False]*(N+1)
dist = [0]*(N+1)

from collections import deque
q = deque([1])
in_queue[1] = True
while q:
    cur = q.popleft()
    # in_queue[cur] = True
    for nxt in adj[cur]:
        if not in_queue[nxt]:
            q.append(nxt)
            in_queue[nxt] = True
            dist[nxt] = dist[cur] + 1

# print(dist)
max_dist = max(dist)
sum = 0
for x in dist:
    if x == max_dist:
        sum+=1
print(dist.index(max_dist),max_dist,sum)