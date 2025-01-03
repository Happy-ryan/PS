n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
from copy import deepcopy

def solution(n, m, board):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m

    def find_cheese(k):
        grids = []

        in_queue = [[False for _ in range(m)] for _ in range(n)]

        def bfs(r, c):
            grid = []

            dq = deque([])
            dq.append((r, c))
            in_queue[r][c] = True
            grid.append((r, c))

            while dq:
                cr, cc = dq.popleft()
                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] == k:
                        dq.append((nr, nc))
                        in_queue[nr][nc] = True
                        grid.append((nr, nc))

            return grid

        for r in range(n):
            for c in range(m):
                if in_queue[r][c] or board[r][c] == 0:
                    continue
                grid = bfs(r, c)
                grids.append(grid)

        return grids


    def find_out(k):

        in_queue = [[False for _ in range(m)] for _ in range(n)]

        def bfs(r, c):
            grid = []

            dq = deque([])
            dq.append((r, c))
            in_queue[r][c] = True
            grid.append((r, c))

            while dq:
                cr, cc = dq.popleft()
                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] == k:
                        dq.append((nr, nc))
                        in_queue[nr][nc] = True
                        grid.append((nr, nc))

            return grid

        grid = bfs(0, 0) # 가장 자리는 치즈가 존재하지 않음! > 치즈 외부를 전부 구할 수 있음.

        return grid

    def melt(cheese_grids, out_grid):
        
        del_board = [[0 for _ in range(m)] for _ in range(n)]
        
        for grid in cheese_grids:
            for r, c in grid:
                out_cnt, in_cnt = 0, 9
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if in_range(nr, nc) and board[nr][nc] == 0:
                        if (nr, nc) in out_grid: # out_grid로 내외부 판단
                            out_cnt += 1
                        else:
                            in_cnt -= 1
                if out_cnt >= 2: # 외부가 2개이상일때만 삭제
                    del_board[r][c] = -1
                    
                    
        new_board = [[0 for _ in range(m)] for _ in range(n)]
        
        for r in range(n):
            for c in range(m):
                new_board[r][c] = board[r][c] + del_board[r][c]
            
        return new_board
    
    
    def one_time():
        cheese_grids = find_cheese(1)
        out_grid = find_out(0)
        new_board = melt(cheese_grids, out_grid)
        if len(cheese_grids) == 0:
            return False
        return new_board


    def end():
        for r in range(n):
            for c in range(m):
                if board[r][c] != 0:
                    return False
        return True

    t = 0
    while True:
        board = one_time()
        if not board:
            return t
        t += 1 
        
    # t = 0
    # while True:
    #     t += 1 
    #     board = one_time()
    #     if end():
    #         return t
        

print(solution(n, m, board))