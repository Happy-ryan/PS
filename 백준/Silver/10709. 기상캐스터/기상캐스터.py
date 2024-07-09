h, w = map(int, input().split())
sky = [list(input()) for _ in range(h)]

def solution(h, w, sky):
    
    board = [[-1 for _ in range(w)] for _ in range(h)]
    
    def find_cloud(sky):
        grids = []
        
        for r in range(h):
            for c in range(w):
                if sky[r][c] == 'c':
                    grids.append((r, c))
        
        return grids
    
    
    def is_stop(sky):
        
        for r in range(h):
            for c in range(w):
                if sky[r][c] == 'c':
                    return False
        
        return True
       
        
    def move_cloud(cloud_grids):
        
        new_sky = [['.' for _ in range(w)] for _ in range(h)]
        
        for r, c in cloud_grids:
            nr = r
            nc = c + 1
            if 0 <= nr < h and 0 <= nc < w:
                new_sky[nr][nc] = 'c'
                
        
        return new_sky
    
    
    def write_board(t, cloud_grid):
        for r, c in cloud_grid:
            if board[r][c] == -1:
                board[r][c] = t
            elif board[r][c] > 0:
                board[r][c] = min(board[r][c], t)
    
    t = 0
    while True:
        if is_stop(sky):
            return board
        
        cloud_grid = find_cloud(sky)
        write_board(t, cloud_grid)
        
        sky = move_cloud(cloud_grid)
        t += 1
        

for row in solution(h, w, sky):
    print(*row)