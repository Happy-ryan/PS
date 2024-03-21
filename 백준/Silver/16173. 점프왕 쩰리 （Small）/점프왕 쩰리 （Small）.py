from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def solution(n, board):
    dr = [1, 0]
    dc = [0, 1]

    visited = [[False for _ in range(n)] for _ in range(n)]

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n

    def bfs():

        dq = deque([])

        dq.append((0, 0))
        visited[0][0] = True

        while dq:
            cr, cc = dq.popleft()
            for k in range(2):
                nr = cr + dr[k] * board[cr][cc]
                nc = cc + dc[k] * board[cr][cc]
                if in_range(nr, nc) and not visited[nr][nc]:
                    dq.append((nr, nc))
                    visited[nr][nc] = True
    bfs()

    if visited[n - 1][n - 1]:
        return "HaruHaru"
    else:
        return "Hing"


print(solution(n, board))