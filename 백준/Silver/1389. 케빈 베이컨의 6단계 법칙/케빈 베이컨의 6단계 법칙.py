from collections import deque

N, M = map(int, input().split())
adj = [[] for col in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

inf = int(1e8)


def bfs(adj ,start):
    dist = [inf for _ in range(N + 1)]
    in_queue = [False for _ in range(N + 1)]

    q = deque([start])
    in_queue[start] = True
    dist[start] = 0

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if not in_queue[nxt]:
                q.append(nxt)
                in_queue[nxt] = True
                dist[nxt] = dist[cur] + 1
    
    return dist

res = []
for k in range(1, N + 1):
    res.append((k, sum(bfs(adj, k)[1:])))

res.sort( key = lambda x : (x[1], x[0]))

print(res[0][0])