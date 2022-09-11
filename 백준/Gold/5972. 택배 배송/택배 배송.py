import sys
from heapq import heappop,heappush

input = sys.stdin.readline

N,M = map(int,input().split())

adj = [[] for row in range(N+1)]
for _ in range(M):
  a,b,c = map(int,input().split())
  adj[a].append((b,c))
  adj[b].append((a,c)) # 노드, 비용

inf = int(1e18)
dist = [inf for col in range(N+1)]

heap = []
heappush(heap,(0,1)) # 비용, 노드
dist[1] = 0

while heap:
  d, cur = heappop(heap)

  if dist[cur] != d: continue

  for nxt, cost in adj[cur]:
    if dist[nxt] > d + cost:
      dist[nxt] = d + cost
      heappush(heap,(dist[nxt],nxt))

print(dist[-1])