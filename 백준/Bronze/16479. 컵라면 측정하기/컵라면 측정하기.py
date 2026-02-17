k = float(input())
d1, d2 = map(float, input().split())

diff = (d1 - d2) / 2

h = k ** 2 - diff ** 2
print(h)