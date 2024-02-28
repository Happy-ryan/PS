from heapq import heappush, heappop

n, m, k = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    adj[a].append((cost, b))
    adj[b].append((cost, a))


def solution(n, m, k, adj):
    
    def dijkstra(start):
        
        inf = int(1e18)
        # k - 포장도로의 수를 의미한다!
        visited = [[inf for _ in range(k + 1)] for _ in range(n + 1)]

        
        heap = []
        # (비용, 지점, 포장도로 개수)
        heappush(heap, (0, start, 0))
        visited[start][0] = 0
        
        while heap:
            d, cur, ck = heappop(heap)
            
            if d > visited[cur][ck]:
                continue
            
            for nd, nxt in adj[cur]:
                # 포장안했어...
                if visited[nxt][ck] > d + nd:
                    visited[nxt][ck] = d + nd
                    heappush(heap, (visited[nxt][ck], nxt, ck))
                # 포장을 했어..
                nk = ck + 1
                if nk < k + 1 and visited[nxt][nk] > d + 0:
                    visited[nxt][nk] = d + 0
                    heappush(heap, (visited[nxt][nk], nxt, nk))
                
        return visited
    
    return min(dijkstra(1)[n])
    
print(solution(n, m, k, adj))