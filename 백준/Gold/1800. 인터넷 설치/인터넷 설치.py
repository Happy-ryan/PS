n, p, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(p)]

def soluiton(n, p, k, edges):
    
    # 인접행렬 - 양방향
    adj = [[] for _ in range(n + 1)]
    for u, v, c in edges:
        adj[u].append((c, v))
        adj[v].append((c, u))
    
    # 초기값 - 연결시킬 때 드는 비용 중 최고 값을 제외한 최고 값
    # 케이블 공짜로 연결!!
    inf = int(1e18)
    dist = [[inf for _ in range(n + 1)] for _ in range(k + 1)]
    
    def dijkstr(s, e):
        
        from heapq import heappop, heappush
        
        heap = []
        dist[0][s] = 0
        heappush(heap, (0, 0, s)) # (비용, 노드)
        
        while heap:
            ck, cd, cur = heappop(heap)
            
            if dist[ck][cur] < cd:
                continue
            
            for cost, nxt in adj[cur]:
                nd = max(cost, cd) # 비용이 최대인 것 중에
                if dist[ck][nxt] > nd:
                    dist[ck][nxt] = nd
                    heappush(heap, (ck, dist[ck][nxt], nxt))
                    
                nk = ck + 1 # 공짜
                
                if nk > k:
                    continue
            
                if dist[nk][nxt] > cd:
                    dist[nk][nxt] = cd
                    heappush(heap, (nk, dist[nk][nxt], nxt))
    
    dijkstr(1, n)
    answer = inf
    for row in dist:
        answer = min(answer, row[n]) # 최소 찾기
        
    return -1 if answer == inf else answer

print(soluiton(n, p, k, edges))