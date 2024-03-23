n, m = map(int, input().split())
start = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
    
from heapq import heappush, heappop
    
def solution(n, m, start, adj):
    inf = int(1e18)
    
    visited = [inf for _ in range(n + 1)]
    
    def di(start):
        
        heap = []
        visited[start] = 0
        heappush(heap, (0, start))
        
        while heap:
            d, cur = heappop(heap)
            
            if d > visited[cur]:
                continue
            
            for nd, nxt in adj[cur]:
                if visited[nxt] > nd + d:
                    visited[nxt] = nd +d
                    heappush(heap, (nd + d, nxt))
        
    di(start)
    
    for i in range(1, n + 1):
        if visited[i] == inf:
            print('INF')
        else:
            print(visited[i])
    

solution(n, m, start, adj)