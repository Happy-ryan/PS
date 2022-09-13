import sys
from heapq import heappop,heappush

input = sys.stdin.readline

V,E,P = map(int,input().split())
adj = [[] for row in range(V+1)]
for _ in range(E):
  a,b,c = map(int,input().split())
  adj[a].append((b,c))
  adj[b].append((a,c))

def dijkstra(adj,s,e):
  inf = int(1e18)
  dist = [inf for col in range(V+1)]
  par = [0 for col in range(V+1)]
  heap = []
  heappush(heap,(0,s))
  dist[s] = 0

  while heap:
    d, cur = heappop(heap)

    for nxt, cost in adj[cur]:
      if dist[nxt] > d + cost:
        dist[nxt] = d + cost
        par[nxt] = cur
        heappush(heap,(dist[nxt],nxt))

    ans = dist[e]

    path= []
    path.append(e)

  while path[-1] != s:
    p = par[e]
    path.append(p)
    e = p

  return ans,par,path

# print(dijkstra(adj,1,V))
# print(dijkstra(adj,1,P))
# print(dijkstra(adj,P,V))

if dijkstra(adj,1,V)[0] == dijkstra(adj,1,P)[0] + dijkstra(adj,P,V)[0]:
  print('SAVE HIM')
else:
  print('GOOD BYE')