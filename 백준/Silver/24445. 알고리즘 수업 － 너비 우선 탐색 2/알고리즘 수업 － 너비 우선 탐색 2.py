n,m,r = map(int,input().split())
adj = [[] for row in range(n+1)]
for i in range(1,m+1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

# print(adj)

for i in range(1,n+1):
    adj[i] = sorted(adj[i])[::-1]

# print(adj)

in_queue = [False] *(n+1)

from collections import deque
q = deque([r])
in_queue[r] = True
result = [0]
while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in adj[cur]:
        if not in_queue[nxt]:
            q.append(nxt)
            in_queue[nxt] = True

# print(result)
ans=[0]*(n+1)
# print('-----------------------')
for i, x in enumerate(result):
    ans[x] = i
for k in ans[1:]:
    print(k)