n, m = map(int, input().split())

if n > m:
    n, m = m, n

print(min(n + m, n + n + 1))