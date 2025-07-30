n = int(input())
m = int(input())
infos = [list(map(int, input().split())) for _ in range(m)]
q = list(map(int, input().split()))

from heapq import heappush, heappop

def solution(n, m, infos, q):
    # 도로간연결 + 거리 최소(최대)비용...다익스트라스러운 느낌..
    
    # 1. 인접행렬
    adj = [[] for _ in range(n + 1)]
    for s, e, c in infos:
        adj[s].append((c, e))
    # par
    par = [-1 for _ in range(n + 1)]
    
    # 2. 변수
    inf = int(1e18)
    # 시작 ~ 도착까지의 최소비용
    dist = [inf for _ in range(n + 1)]
    
    # 3. 다익스트라
    def dijkstra(start, end):
        
        heap =  []
        
        heappush(heap, (0, start))
        dist[start] = 0
        
        while heap:
            cd, cur = heappop(heap)
            
            if dist[cur] < cd:
                continue
            
            for cost, nxt in adj[cur]:
                nd = cost + cd
                if dist[nxt] <= nd:
                    continue
            
                heappush(heap, (nd, nxt))
                dist[nxt] = nd
                par[nxt] = cur
        
        return dist[end]
                
    s, e = q
    cost = dijkstra(s, e)
    
    path = [e]
    while e != s:
        p = par[e]
        path.append(p)
        e = p
    
    path = path[::-1]
    
    print(cost)
    print(len(path))
    print(*path)
        

solution(n, m, infos, q)