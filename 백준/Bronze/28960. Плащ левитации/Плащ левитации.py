h, l, a, b = map(int, input().split())

if (h >= b / 2 and l >= a) or (h >= a / 2 and l >= b):
    print("YES")
else:
    print("NO")