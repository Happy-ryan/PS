n, m, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, k, edges):
    
    adj = [[] for _ in range(n + 1)]
    for u, v, t in edges:
        adj[u].append((t, v))
        adj[v].append((t, u))
        
    # 도로 포장 / 포장 아니냐 > 벽 부수기 처럼 차원 하나 더 추가
    inf = int(1e18)
    dist = [[inf for _ in range(n + 1)] for _ in range(k + 1)]

    def dijkstra(s, e):
    
        from heapq import heappop, heappush
        
        heap = []
        
        dist[0][1] = 0
        heappush(heap, (0, 0, 1)) # 포장, 비용, 노드
        
        while heap:
            ck, cd, cur = heappop(heap)
            
            if dist[ck][cur] < cd: # 갈 곳에 기록된 비용 < 현재 들어갈 비용 : 이동 손해
                continue
            
            for cost, nxt in adj[cur]:
                nd = cost + cd
                if dist[ck][nxt] > nd:
                    dist[ck][nxt] = nd
                    heappush(heap, (ck, nd, nxt))
            
                nk = ck + 1 # 포장함 > 비용 0 무조건 이동 이득!
                
                if nk > k: # 없는 차원
                    continue
                
                if dist[nk][nxt] > 0 + cd:
                    dist[nk][nxt] = 0 + cd
                    heappush(heap, (nk, dist[nk][nxt], nxt))

                    
            
    dijkstra(1, n)
    
    min_ans = inf
    for row in dist:
        min_ans = min(min_ans, row[n])
        
    return min_ans
        
print(solution(n, m, k, edges))