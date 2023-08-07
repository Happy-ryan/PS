n = int(input())

for _ in range(n):
    print("@" * n + " " * (3*n) + "@" * n)
for _ in range(n):
    if n == 1:
        print("@" * n + " " * (2) + "@" * n)
    else:
        print("@" * n + " " * (2*(n - 1) + 2) + "@" * n)
for _ in range(n):
    print("@" * (3 * n))
for _ in range(n):
    if n == 1:
        print("@" * n + " " * (2) + "@" * n)
    else:
        print("@" * n + " " * (2*(n - 1) + 2) + "@" * n)
for _ in range(n):
    print("@" * n + " " * (3*n) + "@" * n)