import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N,M,X = map(int,input().split())
adj = [[] for row in range(N+1)] # X > i 돌아갈 때
radj = [[] for row in range(N+1)] # i > X 도착할 때 역방향으로 생각 i < X

for _ in range(M):
    a,b,c = map(int,input().split())
    adj[a].append((b,c)) # (도착점, 비용)
    radj[b].append((a,c)) 
    

inf = int(1e18)

def dijstrak(S):
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

    return dist

def rdijstrak(S):
    rdist = [inf for col in range(N+1)]
    
    heap = []
    heappush(heap,(0,S))
    rdist[S] = 0

    while heap:
        d,cur = heappop(heap)

        if rdist[cur] != d: continue

        for nxt,cost in radj[cur]:
            if rdist[nxt] > d+cost:
                rdist[nxt] = d+cost
                heappush(heap,(rdist[nxt],nxt))

    return rdist

arr = dijstrak(X)
brr = rdijstrak(X)
result = 0
for i in range(1,N+1):
    result = max(result,arr[i]+brr[i])

print(result)