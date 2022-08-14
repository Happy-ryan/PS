N,M = map(int,input().split()) # N 열 / M 행

adj = [list(input()) for row in range(M)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def adj_check(r,c):
    return 0<= r <= M-1 and 0<= c <= N-1

color_list = ['W','B']
color_num = [0,0]
color_result =[0,0]

# W 판별
for i in range(2):
    visited = [[False for col in range(N)] for row in range(M)]
    def dfs(r,c):
        visited[r][c] = True
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if adj_check(nr,nc) and\
                not visited[nr][nc] and\
                    adj[nr][nc] == color_list[i]:
                    color_num[i] += 1
                    dfs(nr,nc)

    for r in range(M):
        for c in range(N):
            if visited[r][c] or adj[r][c] != color_list[i]:
                continue
            color_num[i] = 1
            dfs(r,c)
            color_result[i] += color_num[i]**2

print(*color_result)