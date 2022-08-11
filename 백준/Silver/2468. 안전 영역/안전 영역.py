import sys
sys.setrecursionlimit(10**4)

n = int(input())
adj =[list(map(int,input().split())) for row in range(n)]
# print(adj)
num_set=set()
for i in range(n):
    for j in range(n):
        num_set.add(adj[i][j])
num_list = [0]+list(num_set)
# print("숫자리스트",num_list) 

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def adj_check(r,c):
    return 0 <= r <= (n-1) and 0 <= c <= (n-1)

def dfs(r,c):
    visited[r][c] = True
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if adj_check(nr,nc) and\
            not visited[nr][nc] and\
                tmp < adj[nr][nc]:
                dfs(nr,nc)

result = set()
for x in num_list:
    tmp = x
    cnt = 0
    visited=[[False for col in range(n)] for row in range(n)]
    for r in range(n):
        for c in range(n):
            if visited[r][c] or adj[r][c] <= tmp:
                continue
            dfs(r,c)
            cnt += 1
    result.add(cnt)

print(max(result))