import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
maps = [list(map(int, input().split())) for row in range(N)]
S, X, Y = map(int, input().split())

in_queue = [[False for col in range(N)] for row in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check(r, c):
    return 0<= r < N and 0<= c < N and\
            not in_queue[r][c] and maps[r][c] == 0

q = deque([])

for r in range(N):
    for c in range(N):
        if maps[r][c] != 0:
            q.append((maps[r][c], r, c, 0)) # 바이러스 숫자, 좌표, 좌표, 시간
            in_queue[r][c] = True

# 작은 바이러스부터 bfs되도록 정렬 후 다시 deque 처리
q = deque(sorted(q))

while q:
    num, cr, cc, s = q.popleft()
    if s == S:
        break
    for k in range(4):
        nr = cr + dr[k]
        nc = cc + dc[k]
        if check(nr, nc):
            # 기존 s = 0 일 때 쭉 bfs 돌고 조건에 만족하면 s + 1 된 좌표들이 들어가게 된다.
            # 따라서 S == 1 이면 s == 0일 때만 bfs 돌게 되고 s = 1 인 좌표들은 bfs 돌지 못함
            q.append((num, nr, nc, s + 1)) 
            in_queue[nr][nc] = True
            maps[nr][nc] = num

print(maps[X-1][Y-1])