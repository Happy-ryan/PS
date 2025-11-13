n = int(input())

if n == 1:
    print(2)
else:
    p1 = n // 2
    p2 = n - p1
    print((p1 + 1) * (p2 + 1))