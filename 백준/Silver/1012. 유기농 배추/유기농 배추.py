import sys
sys.setrecursionlimit(10**4)

T = int(input())
for _ in range(T):
    n,m,k = map(int,input().split())

    adj = [[0 for col in range(m)] for row in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        adj[a][b] = 1

    visited = [[False for col in range(m)] for row in range(n)]

    def adj_check(r, c):
        return 0 <= r <= n-1 and 0 <= c <= m-1

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    def dfs(r,c):
        visited[r][c] = True
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if adj_check(nr,nc) and \
                not visited[nr][nc] and \
                    adj[nr][nc] == 1:
                    dfs(nr,nc)

    result = 0
    for r in range(n):
        for c in range(m):
            if adj[r][c] == 0 or visited[r][c]:
                continue
            dfs(r,c)
            result +=1

    print(result)