N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
A, B = map(int, input().split())

# 다익스트라 - max heap
from heapq import heappush, heappop

def solution(N, M, edges, A, B):
    
    # 인접행렬
    adj = [[] for _ in range(N + 1)]
    for u, v, w in edges:
        adj[u].append((w, v)) # 무게, 노드
        adj[v].append((w, u)) 
    
    # 옮길 수 있는 중량의 최대값..
    inf = int(1e18)
    weights = [-inf for _ in range(N + 1)] # 최대무게니까 -inf
    def dijkstra(A, B):
        
        heap = []
        weights[A] = inf
        heappush(heap, (-inf, A)) # 무게 노드 > max_heap 이라서 -inf
        
        while heap:
            cw, cur = heappop(heap)
            cw = -cw # max_heap (양수로 돌리기)
            
            if weights[cur] > cw: # weight[cur]보다 작은건 의미 없음.
                continue
            
            for w, nxt in adj[cur]:
                nw = min(cw, w) # 경로 상 최소 무게가 새로운 문제가 됨.
                if weights[nxt] < nw:
                    weights[nxt] = nw
                    heappush(heap, (-nw, nxt))
                    
        return weights
        
    dijkstra(A, B)
    
    
    return weights[B]


print(solution(N, M, edges, A, B))