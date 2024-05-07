n, m = map(int, input().split())
s, e = map(int, input().split())
tel = [list(map(int, input().split())) for _ in range(m)]

from collections import deque

def solution(n, m, s, e, tel):
    
    spots = [[] for _ in range(n + 1)]
    for a, b in tel:
        a -= 1
        b -= 1
        spots[a].append(b)
        spots[b].append(a)
    
    # print(spots)
    inf = int(1e18)
    
    dq = deque([])
    visited = [False for _ in range(n + 1)]
    dist = [inf for _ in range(n + 1)]
    
    def bfs():
        
        dq.append(s)
        visited[s] = True
        dist[s] = 0
        
        while dq:
            cx = dq.popleft()
            go = spots[cx] 
            go.append(cx + 1)
            go.append(cx - 1)
            for nx in go:
                if 0 <= nx < n and not visited[nx]:
                    dq.append(nx)
                    visited[nx] = True
                    dist[nx] = dist[cx] + 1
    
    bfs()
    # print(dist)
    
    return dist[e]    

print(solution(n, m, s - 1, e - 1, tel))