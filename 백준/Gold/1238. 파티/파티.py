n, m, x = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, x, edges):
    # 단방향
    adj = [[] for _ in range(n + 1)]
    # 역방향도 필요
    # radj = [[] for _ in range(n + 1)]
    for u, v, c in edges:
        adj[u].append((c, v)) # 비용, 노드
    #   radj[v].append((c, u)) <= 양방향처럼 작용함.
    
    inf = int(1e18)
    
    def dijkstra(s, e, adj):
        
        from heapq import heappop, heappush
        
        heap = []
        dist = [inf for _ in range(n + 1)]
        
        dist[s] = 0
        heappush(heap, (0, s)) # 비용, 노드
        
        while heap:
            cd, cur = heappop(heap)
            
            if dist[cur] < cd:
                continue
            
            for cost, nxt in adj[cur]:
                nd = cd + cost
                if dist[nxt] > nd:
                    dist[nxt] = nd
                    heappush(heap, (nd, nxt))
        
        return dist
    
    answer = -inf
    
    for i in range(1, n + 1):
        dist = dijkstra(i, x, adj)
        rdist = dijkstra(x, i, adj)
        # print(dist)
        # print(rdist)
        answer = max(answer, dist[x] + rdist[i])
        # print(dist[x] + rdist[i])
        # print("-")
    
    return answer

print(solution(n, m, x, edges))