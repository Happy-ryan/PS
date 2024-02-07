# https://www.acmicpc.net/problem/1992

n = int(input())
board = [list(input()) for _ in range(n)]

    
def can_compress(r, c, w):
    standard = board[r][c]
    for i in range(r, r + w):
        for j in range(c, c + w):
            if standard != board[i][j]:
                return False
    return True


stack = []
def DC(r, c, w):
    if can_compress(r, c, w):
        stack.append(board[r][c])
        return

    stack.append('(')
    DC(r, c, w // 2)
    DC(r, c + w // 2, w // 2)
    DC(r + w // 2, c, w // 2)
    DC(r + w // 2, c + w // 2, w // 2)
    stack.append(')')

DC(0, 0, n)
print(''.join(stack))