# 깊이가 (1, 2, 3, 4,) 5인 트리가 존재 - 백트래킹 > 1 ~ n번까지 전부 확인해야함
n, m = map(int, input().split())
adj = [[] for col in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False for col in range(n)]

# 정답 변수 생성
ans = 0
# DFS
def dfs(lev, cur):
    global ans
    if lev == 5:
        ans = 1
        return

    for nxt in adj[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(lev + 1, nxt)
            visited[nxt] = False

for cur in range(n):
    visited[cur] = True 
    dfs(1, cur)
    visited[cur] = False

print(ans)