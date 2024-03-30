n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

from collections import deque


def solution(n, m, board):
    inf = int(1e18)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 물의 이동 후 고슴도치 이동
    # 예전에 풀었던 불과 비슷한 문제!
    # 물의 도착시간과 고슴도치의 도착시간을 비교하자!

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m

    def bfs(starts):
        can_move = [".", "S"]

        visited = [[False for _ in range(m)] for _ in range(n)]
        times = [[inf for _ in range(m)] for _ in range(n)]
        dq = deque([])

        for start in starts:
            r, c = start
            dq.append((r, c))
            visited[r][c] = True
            times[r][c] = 0

        while dq:
            cr, cc = dq.popleft()

            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if (
                    in_range(nr, nc)
                    and not visited[nr][nc]
                    and (board[nr][nc] in can_move)
                ):
                    dq.append((nr, nc))
                    visited[nr][nc] = True
                    times[nr][nc] = times[cr][cc] + 1
        return times

    def find_grid():
        waters = []
        gosumdochi = []
        bibber = []
        for r in range(n):
            for c in range(m):
                if board[r][c] == "*":
                    waters.append((r, c))
                elif board[r][c] == "S":
                    gosumdochi.append((r, c))
                elif board[r][c] == "D":
                    bibber.append((r, c))
        return waters, gosumdochi, bibber

    waters, gosumdochi, bibber = find_grid()
    water_time = bfs(waters)
    gosumdochi_time = bfs(gosumdochi)

    r, c = bibber[0]
    min_time = inf
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if in_range(nr, nc) and gosumdochi_time[nr][nc] < water_time[nr][nc]:
            min_time = min(gosumdochi_time[nr][nc] + 1, min_time)

    if min_time >= inf:
        return "KAKTUS"

    return min_time


print(solution(n, m, board))
