board = [list(map(int, input().split())) for _ in range(19)]

def check(r, c):
    return 0 <= r < 19 and 0 <= c < 19

def check_gomoku(r, c, dr, dc):
    if check(r - dr, c - dc) and board[r][c] == board[r - dr][c - dc]:
        return False
    cnt = 0
    for i in range(6):
        if not check(r + i * dr, c + i * dc) or board[r][c] != board[r + i * dr][c + i * dc]:
            break
        cnt += 1
    return True if cnt == 5 else False

for r in range(19):
    for c in range(19):
        if board[r][c] and (check_gomoku(r, c, 1, 0) or check_gomoku(r, c, 0, 1) \
                            or check_gomoku(r, c, 1, 1) or check_gomoku(r, c, -1, 1)):
            print(board[r][c])
            print(r + 1, c + 1)
            exit(0)
print(0)