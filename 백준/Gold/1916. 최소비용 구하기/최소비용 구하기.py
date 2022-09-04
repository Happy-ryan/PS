import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
M = int(input())
adj = [[] for row in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    adj[a].append((b,c)) #도착점, 비용

S,E = map(int,input().split())

inf = int(1e18)
dist = [inf for col in range(N+1)]

heap = []
heappush(heap,(0,S)) # 비용, 위치
dist[S] = 0

while len(heap) != 0:
    d, cur = heappop(heap) #비용, 위치

    if dist[cur] != d: continue

    for nxt,cost in adj[cur]:
        if dist[nxt] > d+cost:
            dist[nxt] = d+cost
            heappush(heap,(dist[nxt],nxt))

print(dist[E])