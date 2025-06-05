import math

w, h = map(int, input().split())
n, a, b = map(int, input().split())

x = w // a
y = h // b

if a > w or b > h:
    print(-1)
else:
    print(math.ceil(n / (x * y)))