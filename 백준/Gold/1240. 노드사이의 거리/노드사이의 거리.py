from heapq import heappop, heappush

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e, cost = map(int, input().split())
    adj[e].append((cost, s))
    adj[s].append((cost, e))

def bfs(start):
    heap = []
    inf = int(1e9)
    visited = [inf for _ in range(n + 1)]
    
    heappush(heap, (0, start))
    visited[start] = 0
    
    while heap:
        d, cur = heappop(heap)
        
        if d > visited[cur]:
            continue
        
        for nd, nxt in adj[cur]:
            if visited[nxt] > visited[cur] + nd:
                visited[nxt] = visited[cur] + nd
                heappush(heap, (visited[nxt], nxt))
    
    return visited

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s)[e])