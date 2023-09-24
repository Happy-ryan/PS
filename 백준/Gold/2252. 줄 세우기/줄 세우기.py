n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
ind = [0] * (n + 1) # 들어오는 간선의 개수 in-degree

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    ind[y] += 1

candidates = []
for i in range(1, n + 1):
    if ind[i] == 0:
        candidates.append(i)

result = []

while candidates:
    cur = candidates.pop()
    result.append(cur)
    
    for nxt in adj[cur]:
        ind[nxt] -= 1
        if ind[nxt] == 0:
            candidates.append(nxt)

print(*result)
