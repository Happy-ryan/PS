n,m = map(int,input().split()) # n 세로, m 가로

adj = [ list(map(int,input().split())) for row in range(n)]
in_queue = [[False for col in range(m)] for row in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def adj_check(r,c):
    return 0<= r <= n-1 and 0<= c <= m-1

from collections import deque

result = []
for R in range(n):
    for C in range(m):
        if in_queue[R][C]:
            continue
        elif not in_queue[R][C] and adj[R][C] == 0:
            continue
        else:
            q = deque([(R,C)])
            in_queue[R][C] = True
            cnt = 1
            while q:
                r,c = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if adj_check(nr,nc) and\
                        not in_queue[nr][nc] and\
                            adj[nr][nc] == 1:
                            q.append((nr,nc))
                            in_queue[nr][nc] = True
                            cnt += 1
            result.append(cnt)    

if len(result) != 0:
    print(len(result))
    print(max(result))
else:
    print(0)
    print(0)
