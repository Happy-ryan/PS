from collections import deque

n = int(input())
mat = [list(map(int, input().split())) for row in range(n)]

def bfs(h_limit, n, mat):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    in_queue = [[False for col in range(n)] for row in range(n)]

    def check(r, c):
        return 0 <= r < n and 0<= c < n and\
            not in_queue[r][c] and mat[r][c] > h_limit
    
    q = deque([])
    cnts = []
    for r in range(n):
        for c in range(n):
            if in_queue[r][c] or mat[r][c] <= h_limit:
                continue
            q.append((r, c))
            in_queue[r][c] = True
            cnt = 0
            while q:
                cr, cc = q.popleft()
                cnt += 1
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    if check(nr, nc):
                        in_queue[nr][nc] = True
                        q.append((nr, nc))
            cnts.append(cnt)
    
    return len(cnts)

ans = 0
for h in range(101):
    ans = max(ans, bfs(h, n, mat))

print(ans)
