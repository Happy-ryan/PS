import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N,M,X = map(int,input().split())
adj = [[] for row in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    adj[a].append((b,c)) # (도착점, 비용)

inf = int(1e18)

def dijstrak(S,E):
    dist = [inf for col in range(N+1)]

    heap = []
    heappush(heap,(0,S))
    dist[S] = 0

    while heap:
        d,cur = heappop(heap)

        if dist[cur] != d: continue

        for nxt,cost in adj[cur]:
            if dist[nxt] > d+cost:
                dist[nxt] = d+cost
                heappush(heap,(dist[nxt],nxt))

    return dist[E]

result = []
for i in range(1,N+1):
    result.append(dijstrak(i,X)+dijstrak(X,i))

print(max(result))