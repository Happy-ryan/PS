import sys
from heapq import heappop,heappush

input = sys.stdin.readline

n, m = map(int,input().split())
# graph = [[0 for col in range(n)] for row in range(n)]

adj = [[] for row in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  adj[a].append((b,c))
  adj[b].append((a,c))

def dijsktra(adj,s):
  inf = int(1e18)
  dist = [inf for col in range(n+1)]
  par = [0 for col in range(n+1)]

  heap = []
  heappush(heap,(0,s))
  dist[s] = 0

  while heap:
    d, cur = heappop(heap)

    if dist[cur] != d: continue

    for nxt, cost in adj[cur]:
      if dist[nxt] > d + cost:
        dist[nxt] = d + cost
        par[nxt] = cur
        heappush(heap,(dist[nxt],nxt))
  
  # path = []
  # path.append(e)
  # while path[-1] != s:
  #   v = par[e]
  #   path.append(v)
  #   e = v
  # ans = path[-2]

  return par

def f(par,s,e):
  path = []
  path.append(e)
  while path[-1] != s:
    v = par[e]
    path.append(v)
    e = v
  ans = path[-2]
  return ans

for i in range(n):
  result = dijsktra(adj,i+1)
  for j in range(n):
    if i == j:
      print('-', end=' ')
    else:
      print(f(result,i+1,j+1),end=' ')
  print()