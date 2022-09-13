import sys
from heapq import heappop,heappush

input = sys.stdin.readline

n, m, r = map(int,input().split())
items = [0] + list(map(int,input().split()))

adj = [[] for row in range(n+1)]
for _ in range(r):
  a,b,c = map(int,input().split())
  adj[a].append((b,c))
  adj[b].append((a,c))

def dijsktra(adj,s,m,items):
  inf = int(1e18)
  dist = [inf for col in range(n+1)]
  
  heap = []
  heappush(heap,(0,s))
  dist[s] = 0

  while heap:
    d, cur = heappop(heap)

    if dist[cur] != d: continue

    for nxt, cost in adj[cur]:
      if dist[nxt] > d + cost:
        dist[nxt] = d + cost
        heappush(heap,(dist[nxt],nxt))
  sum = 0
  for i in range(1,n+1):
    if dist[i] <= m:
      sum += items[i]

  return sum

ans = 0
for s in range(1,n+1):
  ans = max(ans,dijsktra(adj,s,m,items))

print(ans)