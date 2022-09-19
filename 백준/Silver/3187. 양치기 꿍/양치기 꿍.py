import sys
from collections import deque

input = sys.stdin.readline

R,C = map(int,input().split())

graph = [list(input()) for row in range(R)]
in_queue = [[False for col in range(C)] for row in range(R)]

v_final,k_final = 0,0

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def check(r,c):
  return 0<= r < R and 0<= c <C

def bfs(r,c):
  global k_cnt, v_cnt
  q = deque([(r,c)]) # 시작
  in_queue[r][c] = True

  while q:
    cr, cc = q.popleft()

    for k in range(4):
      nr = cr + dr[k]
      nc = cc + dc[k]

      if check(nr,nc) and\
        not in_queue[nr][nc] and\
          graph[nr][nc] != '#':
          in_queue[nr][nc] = True
          q.append((nr,nc))
          if graph[nr][nc] == 'v':
            v_cnt += 1
          elif graph[nr][nc] == 'k':
            k_cnt += 1

def cnt(v_cnt,k_cnt):
  global k_final, v_final
  if k_cnt > v_cnt:
    k_final += k_cnt
  else:
    v_final += v_cnt 


for i in range(R): # 울타리 안의 공간을 찾아다니기 위해서
  for j in range(C): # bfs는 울타리에 둘려쌓여있을 때 밖으로 나가지 않고 울타리 안에서만 파악함
    if in_queue[i][j]:
      continue
    elif not in_queue[i][j] and graph[i][j] == '#':
      continue
    else:
      if graph[i][j] == 'v':
        v_cnt = 1
        k_cnt = 0
        bfs(i,j)
        # bfs함수에서 영역 내의 k_cnt와 v_cnt 구하고 탈출 후 비교해서
        # final 값에 저장
        cnt(v_cnt,k_cnt)

      elif graph[i][j] == 'k':
        v_cnt = 0
        k_cnt = 1
        bfs(i,j)
        cnt(v_cnt,k_cnt)
      else:
        v_cnt = 0
        k_cnt = 0
        bfs(i,j)
        cnt(v_cnt,k_cnt)

print(k_final,v_final)