# https://www.acmicpc.net/problem/23812

n = int(input())

for _ in range(1, n + 1):
    print("@" * n +" " * (3 * n) + "@" * n)
for _ in range(1, n + 1):
    print("@" * (5 * n))
for _ in range(1, n + 1):
    print("@" * n +" " * (3 * n) + "@" * n)
for _ in range(1, n + 1):
    print("@" * (5 * n))
for _ in range(1, n + 1):
    print("@" * n +" " * (3 * n) + "@" * n)
