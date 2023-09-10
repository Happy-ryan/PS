# x1 y1
# x2 y1
# x1 y2
# x2 y2
# 각 2개씩 존재함. 
# 1개면 추가해야함.

xs, ys = [], []

for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

for i in range(3):
    if xs.count(xs[i]) == 1:
        x4 = xs[i]
    if ys.count(ys[i]) == 1:
        y4 = ys[i]

print(x4, y4)