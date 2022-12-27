
import sys
from heapq import heappop, heappush

N = int(input())
M = int(input())
adj = [[] for row in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    adj[s].append((e,c)) # adj (위치, 비용)

inf = int(1e18)

def dijkstra(s):
    dist = [inf for _ in range(N+1)]
    heap = [] # heap(비용, 위치)
    heappush(heap, (0,s))
    dist[s] = 0

    while heap:
        d, cur  = heappop(heap)

        if dist[cur] != d: continue

        for nxt, cost in adj[cur]:
            if dist[nxt] > d + cost:
                dist[nxt] = d + cost
                heappush(heap, (dist[nxt], nxt))

    for k in range(1, N+1):
        if dist[k] == inf:
            dist[k] =0

    return dist

for k in range(1, N+1):
    print(*dijkstra(k)[1:])