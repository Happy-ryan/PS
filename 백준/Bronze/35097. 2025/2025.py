while True:
    n = int(input())
    if n == 0:
        break
    s = n * (n + 1) // 2
    print(s * s)
