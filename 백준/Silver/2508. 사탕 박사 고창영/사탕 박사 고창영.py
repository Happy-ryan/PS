t = int(input())

def solution(n, m, board):
    change_board = []
    
    def row_col_change():
        for c in range(m):
            row = ''
            for r in range(n):
                row += board[r][c]
            change_board.append(row)
            row = ''
        
    def row_candy(board, candy):
        cnt = 0
        for row in board:
                cnt += row.count(candy)
        return cnt
    
    row_col_change()
    
    return row_candy(board, '>o<') + row_candy(change_board, 'vo^')
    
for _ in range(t):
    input()
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    print(solution(n, m, board))