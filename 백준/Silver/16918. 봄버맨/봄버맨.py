N, M, k = map(int, input().split())
board = [list(input()) for _ in range(N)]


def solution(N, M, k, board):
    
    dr = [-1, 1, 0, 0, 0]
    dc = [0, 0, -1, 1, 0]
    
    all_bomb_board = [['O' for _ in range(M)] for _ in range(N)]
    
    if k == 1:
        for row in board:
            print(''.join(row))
        return
    
    if k % 2 == 0:
        for row in all_bomb_board:
            print(''.join(row))
        return
    
    
    def in_range(r, c):
        return 0 <= r < N and 0 <= c < M
        
        
    def find_bomb_grid(board):
        bomb_grid = []
        for r in range(N):
            for c in range(M):
                if board[r][c] == 'O':
                    bomb_grid.append((r, c))
        
        return bomb_grid
        
        
    def board_bomb_after(bomb_grid):
        after_board = [['O' for _ in range(M)] for _ in range(N)]
        for cr, cc in bomb_grid:
            for k in range(5):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc):
                    after_board[nr][nc] = '.'
        
        return after_board
    
    # print('시간: ', 1)
    # for row in board:
    #     print(''.join(row))
    t = 2
    while True:
        if t == k + 1:
            for row in board:
                print(''.join(row))
            return 
        if t % 2 != 0:
            bomb_grid = find_bomb_grid(board)
            board = board_bomb_after(bomb_grid)

            # print(f"시간: {t}")
            # for row in board:
            #     print(*row)
            # print("-")
        t += 1
            
solution(N, M, k, board)