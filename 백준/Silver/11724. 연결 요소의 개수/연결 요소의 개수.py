n,m = map(int,input().split())
adj = [[] for row in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False]*(n+1)

def dfs(cur):
    # 현재 노드 방문 체크
    visited[cur] = True
    # 연결된 노드 방문
    for nxt in adj[cur]:
        if not visited[nxt]:
            dfs(nxt)

cnt = 0
# 모든 노드를 순회했을 때 방문하지 않은 노드가 존재하면
# dfs 들어가서 연결된 노드 전부 탐색하고 나온다.
# dfs 나오고 +1 한다.
for k in range(1,n+1):
    if not visited[k]:
        dfs(k)
        cnt += 1
print(cnt)
