# https://www.acmicpc.net/problem/19532
# 방정식 해의 범위 : -999~999 : 2000개 > 브루트포스 충분
# x : 2000
# y : 2000
# (x, y) 4000000


def f(a, b, c, x, y):
    flag = False
    if a * x + b * y == c:
        flag = True
    return flag


a1, b1, c1, a2, b2, c2 = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        f1 = f(a1, b1, c1, x, y)
        f2 = f(a2, b2, c2, x, y)
        if f1 == True and f2 == True:
            print(x, y)
