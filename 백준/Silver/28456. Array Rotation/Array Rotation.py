n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
q_n = int(input())
qs = [list(map(int, input().split())) for _ in range(q_n)]

def command_1(board, row):
    x = board[row].pop()
    board[row] = [x] + board[row]
    return board

def command_2(board):
    new_board = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_board[j][n - i - 1] = board[i][j]

    return new_board

for q_row in qs:
    if q_row[0] == 1:
        board = command_1(board, q_row[1] - 1)
    else:
        board = command_2(board)

for row in board:
    print(*row)