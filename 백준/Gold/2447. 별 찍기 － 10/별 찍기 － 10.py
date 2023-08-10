# https://www.acmicpc.net/problem/2447

n = int(input())
board = [[" " for _ in range(n)] for _ in range(n)]

def f(k, r, c):
    if k == 3:
        for y in range(3):
            board[r + y][c] = '*'
        for y in range(3):
            board[r + y][c + 2] = '*'
        for x in range(1, 2):
            board[r][c + x] = '*'
        for x in range(1, 2):
            board[r + 2][c + x] = '*'  
        return
    # k = 9 일때 한 변의 길이 9 정사각형을 이루는 작은 정사각형 8개의 한 변의 길이 3 
    # 각 꼭지점의 좌표 (0, 0), (0, 3), (0, 6), / (3, 0), (3, 6) / (6, 0), , (6, 3), (6, 6)
    # (r, c)     (r,c + d)   (r, c + 2d)
    # (r + d, c)             (r + d, c + 2d)
    # (r + 2d, c) (r+2d, c + d)  (r + 2d, c + 2d)
    d = k // 3
    
    f(k//3, r, c)
    f(k//3, r, c + d)
    f(k//3, r, c + 2 * d)
    f(k//3, r + d, c)
    f(k//3, r + d, c + 2 * d)
    f(k//3, r + 2 * d, c)
    f(k//3, r + 2 * d, c + d)
    f(k//3, r + 2 * d , c + 2 * d)
    

f(n, 0, 0)

for row in board:
    print(*row, sep="")