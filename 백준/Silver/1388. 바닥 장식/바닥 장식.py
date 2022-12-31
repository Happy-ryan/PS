N, M = map(int, input().split())
board = [input() for row in range(N)]
in_queue = [[False for col in range(M)] for row in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check(r,c):
    return 0<= r < N and 0<= c < M and not in_queue[r][c]

res_A = []
res_B = []

from collections import deque

for r in range(N):
    for c in range(M):
        if in_queue[r][c]:
            continue
        elif not in_queue[r][c] and board[r][c] == '|':
            continue
        else:
            q = deque([(r,c)])
            in_queue[r][c] = True
            cnt_A = 1
            while q:
                r, c = q.popleft()
                if board[r][c] == '-':
                    for k in range(2,4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if check(nr,nc) and\
                            board[nr][nc] == '-':
                            in_queue[nr][nc] = True
                            q.append((nr,nc))
                            cnt_A += 1
            res_A.append(cnt_A)

for r in range(N):
    for c in range(M):
        if in_queue[r][c]:
            continue
        elif not in_queue[r][c] and board[r][c] == '-':
            continue
        else:
            q = deque([(r,c)])
            in_queue[r][c] = True
            cnt_B = 1
            while q:
                cr, cc = q.popleft()
                if board[r][c] == '|':
                    for k in range(0,2):
                        nr = cr + dr[k]
                        nc = cc + dc[k]
                        if check(nr,nc) and\
                            board[nr][nc] == '|':
                            in_queue[nr][nc] = True
                            q.append((nr,nc))
                            cnt_B += 1
            res_B.append(cnt_B)

print(len(res_A)+len(res_B))