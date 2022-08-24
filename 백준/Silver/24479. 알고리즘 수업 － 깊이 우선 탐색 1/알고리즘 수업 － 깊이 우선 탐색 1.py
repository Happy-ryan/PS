import sys
sys.setrecursionlimit(10**5)

n,m,r = map(int,input().split())
adj = [[] for row in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
# print(adj)
for i in range(n):
    adj[i] = sorted(adj[i])

# print(adj)

visited = [False]*(n+1)
result =[0]
def dfs(cur):
    visited[cur] = True
    result.append(cur)
    for nxt in adj[cur]:
        if not visited[nxt]:
            dfs(nxt)
    return result

# print(dfs(r))

ans=[0]*(n+1)
for i, x in enumerate(dfs(r)):
    ans[x] = i
for k in ans[1:]:
    print(k)