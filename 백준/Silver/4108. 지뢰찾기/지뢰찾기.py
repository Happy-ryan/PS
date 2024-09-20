def solution(n, m, board):
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, 1, -1, 1, -1]
    
    new_board = [[0 for _ in range(m)] for _ in range(n)]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    for r in range(n):
        for c in range(m):
            if board[r][c] == '*':
                new_board[r][c] = '*'
                for k in range(8):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if in_range(nr, nc) and board[nr][nc] == '.':
                        new_board[nr][nc] += 1
                        
    for row in new_board:
        print(''.join(map(str, row)))
        

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    board = [list(input()) for _ in range(n)]
    solution(n, m, board)