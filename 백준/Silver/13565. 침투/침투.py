M,N = map(int,input().split()) # M 세로 N 가로

adj = [list(input()) for row in range(M)]
in_queue = [[False for col in range(N)] for row in range(M)]

# print(adj)

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def adj_check(r,c):
    return 0 <= r <= M-1 and 0 <= c <= N-1

from collections import deque

for c in range(N):
    if in_queue[0][c]:
        continue
    elif not in_queue[0][c] and adj[0][c] == '1':
        continue
    else:
        q = deque([(0,c)])
        in_queue[0][c] = True
        while q:
            r,c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if adj_check(nr,nc) and\
                    not in_queue[nr][nc] and\
                    adj[nr][nc] == '0':
                    q.append((nr,nc))
                    in_queue[nr][nc] = True

# print(in_queue[M-1])
if True in in_queue[-1]:
    print("YES")
else: print('NO')