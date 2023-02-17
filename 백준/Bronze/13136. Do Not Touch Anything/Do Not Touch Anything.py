r, c, n = map(int, input().split())

if r % n == 0:
    x = r // n
else:
    x = r // n + 1

if c % n == 0:
    y = c // n
else:
    y = c // n + 1

print(x * y)