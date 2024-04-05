maps = [list(input()) for _ in range(12)]

from collections import deque, defaultdict


def solution(maps):

    cnt = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def in_range(r, c):
        return 0 <= r < len(maps) and 0 <= c < len(maps[0])

    def bfs(r, c, color):

        visited = [[False for _ in range(6)] for _ in range(12)]

        girds = []
        dq = deque([])

        dq.append((r, c))
        visited[r][c] = True
        girds.append((r, c))

        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not visited[nr][nc] and maps[nr][nc] == color:
                    dq.append((nr, nc))
                    visited[nr][nc] = True
                    girds.append((nr, nc))
                    
        return girds

    def bomb():
        is_stop = True

        visited = [[False for _ in range(6)] for _ in range(12)]

        for r in range(12):
            for c in range(6):
                if maps[r][c] == "." or visited[r][c]:
                    continue
                
                color = maps[r][c]
                grid = bfs(r, c, color)
                
                for r, c in grid:
                    visited[r][c] = True
                    
                if len(grid) >= 4:
                    is_stop = False
                    for r, c in grid:
                        maps[r][c] = "."

        return is_stop

    def down():
        # 맨 밑에 칸이 .인 세로줄 중 . 이 아닌 블록을 stack에 담자
        for c in range(6):
            stack = []
            for r in range(11, -1, -1):
                if maps[r][c] != ".":
                    stack.append(maps[r][c])
            # 내리기
            tmp = 0
            for r in range(11, -1, -1):
                if tmp < len(stack):
                    maps[r][c] = stack[tmp]
                    tmp += 1
                else:
                    maps[r][c] = "."

    t = 0
    while True:
        if bomb():
            return t
        down()
        t += 1



print(solution(maps))