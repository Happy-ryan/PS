V, E = map(int, input().split())
K = int(input())
edges = [list(map(int, input().split())) for _ in range(E)]
# u -> v 가중치 w

from heapq import heappop, heappush

def solution(V, E, K, edges):
    adj = [[] for _ in range(V + 1)]

    for edge in edges:
        u, v, w = edge
        adj[u].append((w, v)) # (가중치, 노드)
    
    inf = int(1e18)
    visited = [inf for _ in range(V + 1)]
    
    def dijsktra(start):
        
        heap = []
        heappush(heap, (0, start))
        visited[start] = 0

        while heap:
            cd, cur = heappop(heap)
        
            if cd > visited[cur]: # 현재비용이 이미 방문했던 비용보다 크면 볼 필요 없음.
                continue
                
            for nd, nxt in adj[cur]:
                if visited[nxt] > nd + cd: # 방문할 곳의 비용이 cd + nd보다 커야 최적화 의미 존재. > 최소화 시키는 것
                    visited[nxt] = nd + cd
                    heappush(heap, (nd + cd, nxt))
                    
    dijsktra(K)
    
    for i in range(1, V + 1):
        if visited[i] >= inf:
            print('INF')
        else:
            print(visited[i])
    
solution(V, E, K, edges)