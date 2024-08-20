n = int(input())
grids = [list(map(int, input().split())) for _ in range(n)]

inf = 10001
min_x, max_x, min_y, max_y = inf, -inf, inf, -inf
for grid in grids:
    x, y = grid
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
    
print((max_x - min_x) * (max_y - min_y))