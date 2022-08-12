import sys
sys.setrecursionlimit(10**4)

n,m,k = map(int,input().split()) 
# n-행 / m-열 / k-사각형 수
adj = [[1 for col in range(m)] for row in range(n)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            adj[y][x] = 0
# 0 = > 직사각형이 있는 곳 : 방문할 필요 없는 곳
# 1 = > 직사각형이 없는 곳 : 체크해야하는 부분 : 방문해야하는 곳
# print(adj)
# 방문한 곳 체크
visited=[ [False for col in range(m)] for row in range(n)]
# 이동방향
dr = [-1,1,0,0]
dc = [0,0,-1,1]
# adj의 인접행렬 안에 인덱스 존재하는 판단하는 함수
def adj_check(r,c):
    return 0 <= r <= n-1 and 0 <= c <= m-1

# dfs 시작
def dfs(r,c):
    global cnt
    visited[r][c] = True
    cnt += 1 #(중요) 방문할 때마다 더하기 
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if adj_check(nr,nc) and\
            not visited[nr][nc] and\
                adj[nr][nc] != 0:
                dfs(nr,nc)

result = []
for r in range(0,n):
    for c in range(0,m):
        if visited[r][c] or adj[r][c] == 0:
            continue
        cnt = 0
        dfs(r,c)
        result.append(cnt)
result.sort()
print(len(result))
print(*result)