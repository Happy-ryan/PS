n = int(input())
m = int(input())
adj = [[] for row in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

in_queue = [False]*(n+1)
dist = [0]*(n+1)

from collections import deque
q = deque([1])
in_queue[1] = True
while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if not in_queue[nxt]:
            q.append(nxt)
            in_queue[nxt] = True
            dist[nxt] = dist[cur] + 1

# print(dist)
sum = 0
for x in dist:
    if 1<= x <= 2:
        sum += 1
print(sum) 