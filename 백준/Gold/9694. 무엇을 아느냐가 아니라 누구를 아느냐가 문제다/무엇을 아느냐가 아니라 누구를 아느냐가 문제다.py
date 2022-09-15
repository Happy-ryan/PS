
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
inf = int(1e18)

def dijsktra(adj,s,e):

  inf = int(1e18)
  dist = [inf for col in range(M)]
  par = [ 0 for col in range(M)]

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
  
  return dist[e],par

def f_par(par,s,e):
  path = []
  path.append(e)

  while path[-1] != s:
    v = par[e]
    path.append(v)
    e = v
  
  return path

T = int(input())
for i in range(T):
  N,M = map(int,input().split())

  adj = [[] for row in range(M)]
  for _ in range(N):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

  # print(dijsktra(adj,0,M-1))

  if dijsktra(adj,0,M-1)[0] == inf:
    print(f"Case #{i+1}: -1")
  else:
    ans = f_par(dijsktra(adj,0,M-1)[1],0,M-1)[::-1]
    s = str(ans[0])
    for x in ans[1:]:
      s += ' '+str(x)
    print(f"Case #{i+1}: {s}")