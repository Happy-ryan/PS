x, y, z = map(int, input().split())

c4 = x * (0.229) * (0.324)
a3 = y * (0.297) * (0.42)
a4 = z * (0.21) * (0.297)

ans = 2 * c4 + 2 * a3 + 1 * a4
print(ans)