import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split()) # n 가로 : 열 / m 세로 : 행
graph = [input() for row in range(m)]

inf = int(1e18)
dist = [[inf for col in range(n)] for row in range(m)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

heap = []
heappush(heap, (0,0,0)) # 비용, 행, 열
dist[0][0] = 0

def check(r,c):
  return 0<= r < m and 0<= c < n

while heap:
  d,cur_r,cur_c = heappop(heap)

  if dist[cur_r][cur_c] != d: continue

  for k in range(4):
    nr = cur_r + dr[k]
    nc = cur_c + dc[k]
    if check(nr,nc) and\
      dist[nr][nc] > d + int(graph[nr][nc]):
      dist[nr][nc] = d + int(graph[nr][nc])
      heappush(heap,(dist[nr][nc],nr,nc))

print(dist[m-1][n-1])