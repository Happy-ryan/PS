import sys
sys.setrecursionlimit(10**5)

N = int(input())
adj = [list(input()) for row in range(N)]

visited = [[False for col in range(N)] for row in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def adj_check(r,c):
    return 0<= r <= N-1 and 0<= c <= N-1
# 정상인 : R,G,B 모두 구분
color_list = ['R','G','B']
color_num =[0,0,0]
for i in range(3):
    def dfs(r,c):
        visited[r][c] = True
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if adj_check(nr,nc) and\
                not visited[nr][nc] and\
                    adj[nr][nc] == color_list[i]:
                    dfs(nr,nc)
    color_num[i] = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c] or adj[r][c] != color_list[i]:
                continue
            dfs(r,c)
            color_num[i] += 1

result1 = sum(color_num)
# adj_2 는 deepcopy라서 adj에 영향을 준다. 따라서 result1 먼저 계산하고 R>G 변경하기
adj_2 = adj.copy() # 색맹 G > R로 변경
for r in range(N):
    for c in range(N):
        if adj[r][c] =='G':
            adj_2[r][c] = 'R'

visited = [[False for col in range(N)] for row in range(N)]

color_list = ['R','B']
color_num =[0,0]
for i in range(2):
    def dfs(r,c):
        visited[r][c] = True
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if adj_check(nr,nc) and\
                not visited[nr][nc] and\
                    adj_2[nr][nc] == color_list[i]:
                    dfs(nr,nc)
    color_num[i] = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c] or adj_2[r][c] != color_list[i]:
                continue
            dfs(r,c)
            color_num[i] += 1

result2 = sum(color_num)

print(result1,result2)