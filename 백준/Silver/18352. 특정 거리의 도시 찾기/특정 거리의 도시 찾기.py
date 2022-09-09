import sys
from heapq import heappop,heappush

input = sys.stdin.readline

N,M,K,X = map(int,input().split())

adj = [[] for row in range(N+1)]
for _ in range(M):
  a,b = map(int,input().split())
  adj[a].append((b,1)) # 도착점, 비용

inf = int(1e18)
dist = [inf for col in range(N+1)]

heap = []
heappush(heap,(0,X)) # 비용, 노드
dist[X] = 0

while heap:
  d, cur = heappop(heap)
  
  if dist[cur] != d: continue

  for nxt, cost in adj[cur]:
    if dist[nxt] > d + cost:
      dist[nxt] = d + cost
      heappush(heap,(dist[nxt],nxt))

result = []
for i in range(1,len(dist)):
  if dist[i] == K:
    result.append(i)

if len(result) != 0:
  for x in result:
    print(x)
else:
  print(-1)