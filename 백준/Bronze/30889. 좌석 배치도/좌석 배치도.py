n = int(input())
infos = [input() for _ in range(n)]

def solution(n, infos):
    
    board = [['.' for _ in range(20)] for _ in range(10)]
    
    for info in infos:
        r, c = info[0], int(info[1:])
        board[ord(r) - 65][c - 1] = 'o'
        
    
    for row in board:
        print(''.join(row))
        
solution(n, infos)