import sys
from heapq import heappop,heappush

input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for row in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  adj[a].append((b,c))

s,e = map(int,input().split())

inf = int(1e18)
dist = [ inf for col in range(n+1) ]
par = [ 0 for col in range(n+1) ]

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
      par[nxt] = cur

print(dist[e])
# print(par)

path = []
path.append(e)
while path[-1] != s:
  v = par[e]
  path.append(v)
  e = v
print(len(path))
for x in reversed(path):
  print(x,end=' ')