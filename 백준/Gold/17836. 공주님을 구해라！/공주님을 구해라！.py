import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int,input().split())
graph = [list(map(int,input().split())) for row in range(N)]

dist = [[0 for col in range(M)] for row in range(N)]
in_queue = [[False for col in range(M)] for row in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def check(r,c):
  return 0<= r < N and 0<= c < M

def find_gram(graph):
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 2:
        return (i,j)

# print(find_gram(graph))

def bfs(r,c):
  q = deque([(r,c)])
  in_queue[r][c] = True

  while q:
    cr, cc = q.popleft()

    for k in range(4):
      nr = cr + dr[k]
      nc = cc + dc[k]
      if check(nr,nc) and\
        not in_queue[nr][nc] and\
          graph[nr][nc] != 1:
          in_queue[nr][nc] = True
          dist[nr][nc] = dist[cr][cc] + 1
          q.append((nr,nc))
  
  return dist[find_gram(graph)[0]][find_gram(graph)[1]]

def eat_gram(r,c):
  res = N -r -1 + M - c -1
  return res

bfs(0,0) # 함수 호출을 하지 않아서 ans가 0이 나오는 문제가 발생했음..
ans = dist[N-1][M-1]
# print(ans)

if bfs(0,0) == 0: # 그람 도달 불가
  if ans == 0: # 도착점 도달 불가
    print('Fail')
  else: # 도착점 도달 가능
    if ans <= T:
      print(ans)
    else: print('Fail')
else: # 그람 도달 가능
  fr,fc = find_gram(graph)[0],find_gram(graph)[1]
  ans1 = dist[fr][fc]
  ans2 = eat_gram(fr,fc)
  if ans == 0:
    if (ans1+ans2)<= T:
      print(ans1+ans2)
    else: print('Fail')
  else:
    ans3 = min(ans,(ans1+ans2))
    if ans3 <= T:
      print(ans3)
    else: print('Fail')