import sys
from heapq import heappop,heappush

input = sys.stdin.readline

def dijsktra(adj,s):

  inf = int(1e18)
  dist = [ inf for col in range(N+1)]

  heap = []
  heappush(heap,(0,s))
  dist[s] = 0

  while heap:
    d, cur = heappop(heap)

    if dist[cur] != d: continue

    for nxt,cost in adj[cur]:
      if dist[nxt] > d + cost:
        dist[nxt] = d + cost
        heappush(heap,(dist[nxt],nxt))
  
  return dist

T = int(input())

for _ in range(T):
  N,M = map(int,input().split())
  adj = [[]for row in range(N+1)]
  inf = int(1e18)
  res = (inf,0)
  for _ in range(M):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
  K = int(input())
  end_list = list(map(int,input().split()))
  for s in range(1,N+1):
    result = 0
    di = dijsktra(adj,s)
    # print(dijsktra(adj,s))
    for i in range(K):
      result += di[end_list[i]]
  #   result_list.append((result,s))
  # result_list.sort()
  # result_list = result_list[::-1]
    res = min(res,(result,s))
  print(res[-1])