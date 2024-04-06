board = [list(map(int, input().split())) for _ in range(5)]
cr, cc = map(int, input().split())

from collections import deque


def solution(board, cr, cc):

    inf = int(1e18)
    MAX_N = 5
    visited = [[False for _ in range(5)] for _ in range(5)]
    dist = [[inf for _ in range(5)] for _ in range(5)]

    def find():
        for r in range(MAX_N):
            for c in range(MAX_N):
                if board[r][c] == 1:
                    return r, c

    def in_range(r, c):
        return 0 <= r < MAX_N and 0 <= c < MAX_N

    def bfs(r, c):

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        dq = deque([])
        dq.append((r, c))
        visited[r][c] = True
        dist[r][c] = 0

        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] != -1:
                    dq.append((nr, nc))
                    visited[nr][nc] = True
                    dist[nr][nc] = dist[cr][cc] + 1

    bfs(cr, cc)
    grid = find()
    ans = dist[grid[0]][grid[1]]

    if ans >= inf:
        return -1

    return ans


print(solution(board, cr, cc))