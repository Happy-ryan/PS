import sys
from heapq import heappop,heappush

input = sys.stdin.readline

N = int(input())
arr = [ list((input())) for row in range(N)]
graph = [[0 for col in range(N)] for row in range(N)]

# 0-1너비탐색을 하기 위해서 검은방(0) > 1 로 변경
for i in range(N):
  for j in range(N):
    if arr[i][j] == '1':
      graph[i][j] = 0
    else:
      graph[i][j] = 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

inf = int(1e18)
dist = [[inf for col in range(N)] for row in range(N)]

heap = []
heappush(heap,(0,0,0)) # 비용, 행, 열
dist[0][0] = 0

def check(r,c):
  return 0<= r < N and 0<= c < N

while heap:
  d,cur_r,cur_c = heappop(heap)

  if dist[cur_r][cur_c] != d: continue

  for k in range(4):
    nr = cur_r + dr[k]
    nc = cur_c + dc[k]
    if check(nr,nc) and\
      dist[nr][nc] > d + graph[nr][nc]:
      dist[nr][nc] = d + graph[nr][nc]
      heappush(heap,(dist[nr][nc],nr,nc))

print(dist[N-1][N-1])