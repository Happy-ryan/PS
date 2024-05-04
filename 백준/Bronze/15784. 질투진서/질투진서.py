n, r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] 

def solution(n, r, c, board):
    max_handsome = board[r - 1][c - 1]
    
    for i in range(n):
        if max_handsome < board[i][c - 1]:
            return 'ANGRY'
    for j in range(n):
        if max_handsome < board[r - 1][j]:
            return 'ANGRY'
        
    return 'HAPPY'

print(solution(n, r, c, board))