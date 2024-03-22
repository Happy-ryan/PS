# 불의 이동과 사람의 이동 > 불의 이동이 사람의 이동보다 선행된다.
# 불이 도달하기 전에 나가는 것이 포인트!
from collections import deque

def solution(n, m, board):
    inf = int(1e14)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m

    def find_grid():
        fires = []
        person = []
        for r in range(n):
            for c in range(m):
                if board[r][c] == "*":
                    fires.append((r, c))
                elif board[r][c] == "@":
                    person.append((r, c))
        return fires, person

    def find_exit():
        exits = set()
        for r in range(n):
            if board[r][0] != "#":
                exits.add((r, 0))
            if board[r][m - 1] != "#":
                exits.add((r, m - 1))

        for c in range(m):
            if board[0][c] != "#":
                exits.add((0, c))
            if board[n - 1][c] != "#":
                exits.add((n - 1, c))

        return exits

    def bfs(target: list[tuple]):
        visited = [[False for _ in range(m)] for _ in range(n)]
        seconds = [[inf for _ in range(m)] for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if board[r][c] == "#":
                    visited[r][c] = True

        dq = deque([])

        for r, c in target:
            dq.append((r, c))
            visited[r][c] = True
            seconds[r][c] = 1

        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] != "*":
                    dq.append((nr, nc))
                    visited[nr][nc] = True
                    seconds[nr][nc] = seconds[cr][cc] + 1

        return seconds

    fires, person = find_grid()

    exits = find_exit()
    fire_second = bfs(fires)
    person_second = bfs(person)

    flag = False
    min_time = inf
    for r, c in exits:
        if fire_second[r][c] > person_second[r][c]:
            flag = True
            min_time = min(min_time, person_second[r][c])

    if flag:
        return min_time
    else:
        return "IMPOSSIBLE"


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    print(solution(n, m, board))