x, y, w, h = map(int, input().split())
a = w-x
b = h-y
result = min(a, b, x, y)
print(result)