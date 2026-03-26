n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
s, e = map(int, input().split())

def solution(n, m, edges, s, e):
    adj = [[] for _ in range(n + 1)]
    for u, v, c in edges:
        adj[u].append((c, v)) # 비용, 도착점
        
    
    from heapq import heappop, heappush
    
    # 최소비용
    inf = int(1e19)
    
    def dijkstra(s, e):
        
        heap = []
        dist = [inf for _ in range(n + 1)]
        par = [-1 for _ in range(n + 1)]
        
        dist[s] = 0 # 최소비용의 시작은 0
        heappush(heap, (0, s)) # 비용, 지점
        par[s] = 0
        
        while heap:
            cd, cur = heappop(heap)
            
            if dist[cur] < cd: # 이동 손해
                continue
            
            for cost, nxt in adj[cur]:
                nd = cost + cd
                
                if dist[nxt] > nd: # 현재 nxt까지 이동했을 때 기록된 비용 > New 비용 > 이동 이득 
                    dist[nxt] = nd
                    heappush(heap, (nd, nxt))
                    par[nxt] = cur
                    
                    
        min_cost = dist[e]
        path = []
        
        idx = e
        while True:
            path.append(idx)
            if par[idx] == 0:
                break
            idx = par[idx]
            
        print(min_cost)
        print(len(path))
        print(*path[::-1])
                    
    
    dijkstra(s, e)
        
solution(n, m, edges, s, e)