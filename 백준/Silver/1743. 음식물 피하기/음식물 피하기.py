import sys
sys.setrecursionlimit(10**4)

n, m, k = map(int,input().split())
adj = [[0 for col in range(m)] for row in range(n)]
for _ in range(k):
    a,b = map(int,input().split())
    adj[a-1][b-1] = 1
# print(adj)
visited =[[False for col in range(m)] for row in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def adj_check(r,c):
    return 0<= r <= n-1 and 0<= c <= m-1

def dfs(r,c):
    global cnt
    visited[r][c] = True
    cnt += 1
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if adj_check(nr,nc) and\
            not visited[nr][nc] and\
                adj[nr][nc] == 1:
                dfs(nr,nc)

result = 1
for r in range(0,n):
    for c in range(0,m):
        if visited[r][c] or adj[r][c] == 0:
            continue
        cnt = 0
        dfs(r,c)
        result = max(result,cnt)
print(result)