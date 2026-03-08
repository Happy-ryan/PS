n, m, k = map(int, input().split())
grids = [list(map(int, input().split())) for _ in range(k)]

# school = [[0 for _ in range(m + 2)] for _ in range(n)]

food = (n - 1, m + 2 - 1) # 급식실 좌표

inf = int(1e18)
record = (inf, inf)

for idx, grid in enumerate(grids):
    f, d = grid
    d_ = m + 2 - 1 - d
    f_ = n - 1 - n + f
    if record[0] > d_ + f_:
        record = (d_ + f_, idx + 1)
    else:
        if record[0] == d_ + f_:
            if record[1] > idx + 1:
                record = (d_ + f_, idx + 1)
                
print(record[1])