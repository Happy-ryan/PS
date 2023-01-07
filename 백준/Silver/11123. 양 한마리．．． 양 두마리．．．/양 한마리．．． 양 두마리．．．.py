from collections import deque

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    maps = [list(input()) for row in range(R)]

    in_queue = [[False for col in range(C)] for row in range(R)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def check(r, c):
        return 0<= r < R and 0<= c < C and in_queue[r][c] == False

    def bfs(r, c):
        q = deque([(r, c)])
        in_queue[r][c] = True

        while q:
            cr, cc = q.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if check(nr, nc) and maps[nr][nc] == '#':
                    q.append((nr, nc))
                    in_queue[nr][nc] = True
    cnt = 0
    for r in range(R):
        for c in range(C):
            if maps[r][c] == '.' or in_queue[r][c] == True:
                continue
            bfs(r, c)
            cnt += 1
            
    print(cnt)