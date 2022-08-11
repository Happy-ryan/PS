from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    dist = [[0 for col in range(n)] for row in range(n)]
    r1, c1 = map(int,input().split())
    r2, c2 = map(int,input().split())
    # 이동방향
    dr = [-2,-2,2,2,-1,-1,1,1]
    dc = [-1,1,-1,1,2,-2,2,-2]
    # 
    in_queue = [[False for col in range(n)] for row in range(n)]
    #
    def dist_check(r,c):
        return 0 <= r <= n-1 and 0 <= c <= n-1
    #
    dist[r1][c1] = 0
    q = deque([(r1,c1)])
    in_queue[r1][c1] = True
    # bfs 진입
    while len(q)>0:
        r,c = q.popleft()
        for k in range(8):
            nr = r +dr[k]
            nc = c +dc[k]
            if dist_check(nr,nc) and\
                not in_queue[nr][nc]:
                    q.append((nr,nc))
                    in_queue[nr][nc] = True
                    dist[nr][nc] = dist[r][c]+1
    print(dist[r2][c2])