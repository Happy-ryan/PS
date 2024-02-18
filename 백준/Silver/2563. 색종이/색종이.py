n = int(input())
board = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    # 좌표계 변경 행 = n - 1 - y
    c, r = x, 100 - y - 1
    for i in range(r - 10, r):
        for j in range(c, c + 10):
            board[i][j] = 1

cnt = 0
for row in board:
    cnt += sum(row)
print(cnt)