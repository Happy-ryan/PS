n = int(input())
m = int(input())
adj = [[] for row in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
# print(adj)

visited = [0]*(n+1)

def dfs(cur):
    # global cnt
    # 현재 위치 방문 : 문제상 cur는 노드1번에서 시작
    if visited[cur]: return
    visited[cur] = 1 # 방문하면 1
    # 현재 cur에 연결된노드들 nxt 
    # nxt 노드가 방문한 적이 있다면 True로 return 종료
    # nxt 노드가 방문한 적이 없다면 visited[nxt] = True
    for nxt in adj[cur]:
        dfs(nxt)
    return sum(visited)-1

print(dfs(1))