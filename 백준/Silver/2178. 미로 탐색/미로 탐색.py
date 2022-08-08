n,m = map(int,input().split())
# (1,1)에서부터 시작하기 위해서 # 로 벽치기
graph = ['#'*(m+2)]+['#'+input()+'#'for row in range(n)]+['#'*(m+2)]
# print(graph)
# print(graph[1][1])

# bfs를 위해서 deque 사용
from collections import deque

# bfs에서 dfs의 vistied와 유사한 기능을 하는 것을 in_queue로 정의
in_queue =  [[ False for col in range(m+1)] for row in range(n+1)]

# 미로 이동하면서 이동한 거리 저장 dp
dist = [[0 for col in range(m+1)] for row in range(n+1)]

# 현재 (1,1) 위치 체크하기
q = deque([(1,1)])
in_queue[1][1] = True
dist[1][1] = 1

# 이동하기
dr = [-1,1,0,0] # 좌//우
dc = [0,0,-1,1] # 상//하

# 이동했을 때 board안에 있는지 체크
def bound_check(r, c):
    return 1 <= r <= n and 1 <= c <= m

# q가 있을 때까지 체크:
while q:
    r,c = q.popleft()
    for x in range(4):
        nr = r + dr[x]
        nc = c + dc[x]
        # graph 안에 존재 &
        # 1으로 있는 곳만 이동가능 &
        # in_queue 가 False ,즉 방문하지 않은 곳
        if bound_check(nr,nc) and \
            graph[nr][nc] == '1' and \
                not in_queue[nr][nc]:
                q.append((nr,nc))
                in_queue[nr][nc] = True
                dist[nr][nc] = dist[r][c] +1

print(dist[n][m])