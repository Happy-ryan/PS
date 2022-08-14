N,M = map(int,input().split()) # N 열 / M 행

adj = [ list(input()) for row in range(M)]
visited = [[False for col in range(N)] for row in range(M)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def adj_check(r,c):
    return 0<= r <= M-1 and 0<= c <= N-1

color_list = ['W','B']
color_num = [[],[]]

# W 판별
def dfs(r,c):
    global W_num
    visited[r][c] = True
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if adj_check(nr,nc) and\
            not visited[nr][nc] and\
                adj[nr][nc] == 'W':
                W_num += 1
                dfs(nr,nc)

W_cnt =[]
for r in range(M):
    for c in range(N):
        if visited[r][c] or adj[r][c] != 'W':
            continue
        W_num = 1
        dfs(r,c)
        W_cnt.append(W_num**2)

# print(W_cnt)

visited = [[False for col in range(N)] for row in range(M)]

def dfs(r,c):
    global B_num
    visited[r][c] = True
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if adj_check(nr,nc) and\
            not visited[nr][nc] and\
                adj[nr][nc] == 'B':
                B_num += 1
                dfs(nr,nc)


B_cnt =[]
for r in range(M):
    for c in range(N):
        if visited[r][c] or adj[r][c] != 'B':
            continue
        B_num = 1
        dfs(r,c)
        B_cnt.append(B_num**2)
        
print(sum(W_cnt),sum(B_cnt))