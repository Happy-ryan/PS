m = int(input())
n = int(input())

if n == 1 or m == 1:
    print(n * m)
else:
    print(m * n - (m - 2) * (n - 2))