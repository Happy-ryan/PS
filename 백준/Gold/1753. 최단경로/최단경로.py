import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().split())
s = int(input())

INF = 1e18
dist = [INF for _ in range(N + 1)]
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

heap = []
heappush(heap, (0, s))
dist[s] = 0

while len(heap) != 0:
    d, cur = heappop(heap)

    if dist[cur] != d: continue

    for nxt, cost in adj[cur]:
        if dist[nxt] > d + cost:
            dist[nxt] = d + cost
            heappush(heap, (dist[nxt], nxt))

for i in range(1, N + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
