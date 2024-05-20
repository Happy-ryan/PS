n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def solution(n, m, board):
    
    answer = []
    
    def Intensity_function(r, g, b):
        
        i = 2126 * r + 7152 * g + 722 * b
        
        if 0 <= i < 510000:
            return '#'
        if 510000 <= i < 1020000:
            return 'o'
        if 1020000 <= i < 1530000:
            return '+'
        if 1530000 <= i < 2040000:
            return '-'
        if 2040000 <= i:
            return '.'
    
    for i in range(n):
        row = []
        for j in range(0, 3 * m, 3):
            row.append(Intensity_function(board[i][j],board[i][j + 1],board[i][j + 2]))
        answer.append(row)
        
    for row in answer:
        print(''.join(row))
        
solution(n, m, board)