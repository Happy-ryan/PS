# https://www.acmicpc.net/problem/1531

board = [[0 for _ in range(100)] for _ in range(100)]

#(x, y) = (0, 0) -> (r, c) = (100, 0)
#(x, y) = (0, 100) -> (r, c) = (0, 0)
#(x, y) = (100, 0) -> (r, c) = (100, 100)
#(x, y) = (100, 100) -> (r, c) = (0, 100)
#(x, y) = (90, 90) -> (r, c) = (10, 90)
#(x, y) = (60, 60) -> (r, c) = (40, 60)
# 좌표계 -> 격자로 변경
def coordinates_change(x, y):
    r = 100 - y
    c = x
    return(r, c)

n, m = map(int, input().split())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    r1, c1 = coordinates_change(x1, y1)
    r2, c2 = coordinates_change(x2, y2)
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    for r in range(r2, r1 + 1):
        for c in range(c1, c2 + 1):
            board[r][c] += 1
            
sum_val = 0   
for row in board:
    for x in row:
        if x > m:
            sum_val += 1
            
print(sum_val)