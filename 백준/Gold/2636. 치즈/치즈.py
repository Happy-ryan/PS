n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간
# 모두 녹기 한 시간 전에 남아 있는 치즈조각이 놓여있는 칸의 수

# 1. 공기의 영역을 찾기 -> bfs
# 2. 공기 영역 찾은 후 겉에 있는 치즈 -> 공기로 변경하기

from collections import deque


def solution(n, m, board):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m

    def find_air():
        airs = []
        visited = [[False for _ in range(m)] for _ in range(n)]

        dq = deque([])

        dq.append((0, 0))
        airs.append((0, 0))
        visited[0][0] = True

        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == 0:
                    dq.append((nr, nc))
                    airs.append((nr, nc))
                    visited[nr][nc] = True

        return airs

    def change_cheese(airs):
        for r, c in airs:
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr, nc) and board[nr][nc] == 1:
                    board[nr][nc] = 0

    def count_cheese():
        cnt = 0
        for r in range(n):
            for c in range(m):
                if board[r][c] == 1:
                    cnt += 1

        return cnt

    t = 0
    ans = 0
    while True:
        final_cheese = count_cheese()
        if final_cheese == 0:
            break

        airs = find_air()
        change_cheese(airs)
        ans = final_cheese

        t += 1
        
    print(t)
    print(ans)


solution(n, m, board)