n = int(input())

def check(n):
    for _ in range(2 * n):
        print("@" * n + " " * 3 * n + "@" * n)
    for _ in range(n):
        print('@@@@@' * n)
    for _ in range(n):
        print("@" * n + " " * 3 * n + "@" * n)
    for _ in range(n):
        print('@@@@@' * n)

check(n)