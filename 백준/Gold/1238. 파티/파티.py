N, M, X = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

from heapq import heappush, heappop

def solution(N, M, X, edges):
    # 단방향 / 오고가는가는데 가장 오래 걸리는 학생
    
    adj = [[] for _ in range(N + 1)]
    radj = [[] for _ in range(N + 1)]
    
    for u, v, t in edges:
        adj[u].append((t, v)) # 최단거리로 가야하기때문에 최소 시간 구해야함.
        radj[v].append((t, u)) # 양방향처럼 되어버렸음.. <- 이거 쓰면 안돼!
    
    inf = int(1e18)
    
    
    def dijkstra(start, adj, dist):
        
        heap = []
        
        dist[start] = 0
        heappush(heap, (0, start))
        
        while heap:
            cd, cur = heappop(heap)
            
            if dist[cur] < cd:
                continue
            
            for nd, nxt in adj[cur]:
                if dist[nxt] > cd + nd:
                    dist[nxt] = cd + nd
                    heappush(heap, (dist[nxt], nxt))
    # (rdist)시작점1개 + 도착점 여러개 <-> (dist)현 상황 : 시작점 여러개 + 도착점 1개 (도착점 기준 생각)
    # 집에서 파티장 갈 때 : 도착점1개에서 -> 여러집(시작점)으로 가는 최소 비용 
    # 파티절에서 집 갈 때 : 시작점1개 -> 여러집(도착점)
    answer = 0
    dist = [inf for _ in range(N + 1)]
    dijkstra(X, adj, dist) 
    rdist = [inf for _ in range(N + 1)]
    dijkstra(X, radj, rdist)
    
    res = -inf
    for i in range(1, N + 1):
        res = max(res, dist[i] + rdist[i])
    
    return res

print(solution(N, M, X, edges))