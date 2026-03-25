n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

from collections import deque


def solution(n, m, board):

    inf = int(1e14)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
    dist = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(2)]

    def in_range(r, c, k):
        return 0 <= r < n and 0 <= c < m and 0 <= k < 2

    def bfs():

        dq = deque([])
        dq.append((0, 0, 0))
        # k, n, m
        visited[0][0][0] = True
        dist[0][0][0] = 1

        while dq:
            cr, cc, ck = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                # 벽 안 부심.
                if (
                    in_range(nr, nc, ck)
                    and not visited[ck][nr][nc]
                    and board[nr][nc] == 0
                ):
                    dq.append((nr, nc, ck))
                    visited[ck][nr][nc] = True
                    dist[ck][nr][nc] = dist[ck][cr][cc] + 1

                # 벽 부심 > board에서는 벽이 선택되어야함.
                # board = 1
                nk = ck + 1
                if (
                    in_range(nr, nc, nk)
                    and not visited[nk][nr][nc]
                    and board[nr][nc] == 1
                ):
                    dq.append((nr, nc, nk))
                    visited[nk][nr][nc] = True
                    dist[nk][nr][nc] = dist[ck][cr][cc] + 1

    bfs()

    ans = inf
    for i in range(2):
        ans = min(ans, dist[i][-1][-1])

    if ans >= inf:
        ans = -1
        
    return ans

print(solution(n, m, board))