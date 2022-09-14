
import sys
from heapq import heappop, heappush

N = int(input())
friends = list(map(int,input().split()))
M = int(input())
adj = [[] for row in range(N+1)]
for _ in range(M):
  a,b,c = map(int,input().split())
  adj[a].append((b,c))
  adj[b].append((a,c))

def dijsktra(adj,s): 
  inf = int(1e18)
  dist = [ inf for col in range(N+1)]

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

  return dist

# inf = int(1e18)
# ans_tuple = (0,0)

# for s in range(1,N+1):
#   ans = inf
#   if s in friends:
#     continue
#   result = dijsktra(adj,s)
#   for x in friends:
#     ans = min(ans,result[x])
#   ans_tuple= max(ans_tuple,(ans,-s))

# print(-ans_tuple[1])

inf = int(1e18)
ans = [inf]*(N+1)
for x in friends:
  result = dijsktra(adj,x)
  # print(result)
  for i in range(1,N+1):
    ans[i] = min(ans[i],result[i])

max_ans = max(ans[1:])
print(ans.index(max_ans))