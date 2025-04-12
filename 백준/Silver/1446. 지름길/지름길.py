n, d = map(int,input().split())
roads = [list(map(int, input().split())) for _ in range(n)]

from heapq import heappop, heappush

def solution(n, d, roads):
    # 거리의 최솟값 = 다익스트라 느낌 존재
    
    # 도로 그래프 - 지름길
    adj = [[] for _ in range(d + 1)]
    for s, e, c in roads:
        if e > d:
            continue
        adj[s].append((c, e))
    # 도로 그래프 - 일반도로
    for s in range(d):
        adj[s].append((1, s + 1))
    
    inf = int(1e18)
    dist = [inf for _ in range(d + 1)] # S에서 ~ 해당 노드까지 오는데 걸리는 최소 비용
    
    def dijkstra(start):
        
        heap = []
        
        # (비용, 현재위치) -> 정렬 / 최소비용부터 
        heappush(heap, (0, start))
        dist[start] = 0
        
        while heap:
            cd, cur  = heappop(heap)
            
            # 이미 최적화되어있기때문에 다익스트라 안가도 됨.
            if dist[cur] < cd:
                continue
            
            for cost, nxt in adj[cur]:
                nd = cd + cost
                if dist[nxt] <= nd:
                    continue
                
                heappush(heap, (nd, nxt))
                dist[nxt] = nd
                
        return dist[d]
    
    return dijkstra(0)
    
print(solution(n, d, roads))