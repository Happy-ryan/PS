#=================================bfs풀이=====================================
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
in_queue = [ [False for col in range(m)] for row in range(n)]
dist = [[1 for col in range(m)] for row in range(n)]
# 이동방향
dr = [-1,1,0,0]
dc = [0,0,-1,1]
# adj의 인접행렬 안에 인덱스 존재하는 판단하는 함수
def adj_check(r,c):
    return 0 <= r <= n-1 and 0 <= c <= m-1

from collections import deque

result = []
for r in range(n):
    for c in range(m):
        if in_queue[r][c] == True:
            continue
        elif in_queue[r][c] == False and adj[r][c] == 0:
            continue
        else:
            q = deque([(r,c)])
            in_queue[r][c] = True
            cnt = 1
            # bfs 진입 시작
            while q:
                r,c = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if adj_check(nr,nc) and\
                        not in_queue[nr][nc] and\
                            adj[nr][nc] != 0:
                            q.append((nr,nc))
                            in_queue[nr][nc] = True
                            cnt += 1
            result.append(cnt)
result.sort()
print(len(result))
print(*result)
