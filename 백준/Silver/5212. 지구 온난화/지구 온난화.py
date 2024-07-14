n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

def solution(n, m, board):
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def find_water_islane_grid():
        grids = []
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'X':
                    cnt = 0
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if in_range(nr, nc) and board[nr][nc] == '.' or not in_range(nr, nc):
                            cnt += 1
                    if cnt >= 3:
                        grids.append((r, c))
        return grids
    
    def afer_50_year(grids):
        for r, c in grids:
            board[r][c] = '.'
    
    def find_region_grid():
        grids = []
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'X':
                    grids.append((r, c))
        
        return grids
    
    def make_region(grids):
        min_r, min_c = n, m
        max_r, max_c = -1, -1
        
        for r, c in grids:
            min_r = min(min_r, r)
            min_c = min(min_c, c)
            max_r = max(max_r, r)
            max_c = max(max_c, c)
        

        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                print(board[r][c], end='')
            print()
            
            
    water_island_grid = find_water_islane_grid()
    afer_50_year(water_island_grid)
    region_gird = find_region_grid()
    make_region(region_gird)
    
solution(n, m, board)