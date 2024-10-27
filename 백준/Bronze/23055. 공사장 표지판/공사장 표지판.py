n = int(input())

board = [[' ' for _ in range(n)] for _ in range(n)]

for i in range(n):
    # 세로
    board[i][0] = '*'
    board[i][-1] = '*'
    # 가로
    board[0][i] = '*'
    board[-1][i] = '*'
    
    # \
    board[i][i] = '*'
    
    # /
    board[i][-i-1] = '*'

for i in range(n):
    print(''.join(board[i]))
