
import sys
from heapq import heappop,heappush

input = sys.stdin.readline

T = int(input())

def dijsktra():
  n,d,c = map(int,input().split())

  adj = [[] for row in range(n+1)]
  for _ in range(d):
    a,b,s = map(int,input().split())
    adj[b].append((a,s)) # 도착점, 비용

  inf = int(1e18)
  dist = [inf for col in range(n+1)]

  heap = []
  heappush(heap,(0,c)) # 비용, 노드
  dist[c] = 0

  while heap:
    d, cur = heappop(heap)

    if dist[cur] != d: continue

    for nxt,cost in adj[cur]:
      if dist[nxt] > d + cost:
        dist[nxt] = d + cost
        heappush(heap,(dist[nxt],nxt))
  cnt = 0
  result = set()
  for x in dist:
    if x != inf:
      cnt += 1
      result.add(x)

  return [cnt, max(result)]

for _ in range(T):
  print(*dijsktra())