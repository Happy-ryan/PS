import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N,E = map(int,input().split())

adj = [[] for row in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

v1,v2 = map(int,input().split())

inf = int(1e18)
# 출발점에 따라 도착점까지의 최소비용 함수
# 출발점 바뀔 때마다 dist도 초기화해야하므로 함수 안에 넣기
def dijkstra(S,E):
    dist = [inf for col in range(N+1)]
    heap = []
    heappush(heap,(0,S))
    dist[S] = 0

    while heap:
        d, cur = heappop(heap)

        if dist[cur] != d: continue

        for nxt,cost in adj[cur]:
            if dist[nxt] > d + cost:
                dist[nxt] = d+cost
                heappush(heap,(dist[nxt],nxt))

    return dist[E]

result = min(dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,N),\
            dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,N))

if result >= inf:
    print(-1)
else:
    print(result)