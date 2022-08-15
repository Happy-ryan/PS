N, M = map(int, input().split())  # N 세로 M 가로
# print(N)
# print(M)
adj = [list(map(int, input().split())) for row in range(N)]
in_queue = [[False for col in range(M)] for row in range(N)]

# print(adj)

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]


def adj_check(r, c):
    return 0 <= r < N and 0 <= c < M


from collections import deque

result = []
for r in range(N):
    for c in range(M):
        if in_queue[r][c] or adj[r][c] == 0:
            continue
        q = deque([(r, c)])
        in_queue[r][c] = True
        cnt = 0
        while q:
            cr, cc = q.popleft()
            cnt += 1
            for k in range(8):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if adj_check(nr,nc) and \
                    not in_queue[nr][nc] and \
                    adj[nr][nc] == 1:
                    q.append((nr, nc))
                    in_queue[nr][nc] = True
        result.append(cnt)

print(len(result))