n, m, x = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(m)]

from heapq import heappush, heappop

def solution(n, m, x, infos):
    
    # 1. 인접행렬
    adj = [[] for _ in range(n + 1)]
    nadj = [[] for _ in range(n + 1)]
    
    for info in infos:
        s, e, c = info
        adj[s].append((c, e))
        nadj[e].append((c, s))
    
    # 2. 변수
    inf = int(1e18)
    
    # 3. 다익스트라 : 시작점1개 + 도착점 여러개 <-> 현 상황 : 시작점 여러개 + 도착점 1개 (도착점 기준 생각)
    def dijkstra(start, adj, dist):
        
        heap = []
        
        heappush(heap, (0, start))
        dist[start] = 0
        
        while heap:
            cd, cur = heappop(heap)
            
            if dist[cur] < cd:
                continue
            
            for cost, nxt in adj[cur]:
                nd = cd + cost
                if dist[nxt] <= nd:
                    continue
                
                heappush(heap, (nd, nxt))
                dist[nxt] = nd
                
    # x 시작점(도착점=파티), adj(s(파티) -> e(집)): 파티 -> 집
    dist = [inf for _ in range(n + 1)]
    dijkstra(x, adj, dist)
    # x 시작점(도착점), nadj(e -> s): 집 -> 파티
    ndist = [inf for _ in range(n + 1)]
    dijkstra(x, nadj, ndist)
    
    res = -inf
    for i in range(1, n + 1):
        res = max(res, dist[i] + ndist[i])
    
    return res
        
print(solution(n, m, x, infos))