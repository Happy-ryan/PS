a, b, c, d = map(int, input().split())
print(a + b + c + d - min(a, b, c, d) + 1)