n = int(input())

grid = [[0] * 501 for _ in range(501)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    # 실제 행사장의 넓이 구하기 > 겹친 부분 제외
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 1

area = 0
for i in range(501):
    for j in range(501):
        area += grid[i][j]

print(area)