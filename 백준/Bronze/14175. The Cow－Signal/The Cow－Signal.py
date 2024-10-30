r, c, k = map(int, input().split())
board = [list(input()) for _ in range(r)]

def solution(r, c, k, board):
    
        row = ''
        for i in range(r):
            for j in range(c):
                row += board[i][j] * k
            for _ in range(k):
                print(row)
            row = ''
            
solution(r, c, k, board)