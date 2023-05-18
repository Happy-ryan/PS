# https://www.acmicpc.net/submit/23794
n = int(input())
for _ in range(n + 2):
    print("@", end="")
print()
for _ in range(n):
    for i in range(n + 2):
        if i == 0 or i == n + 1:
            print("@", end="")
        else:
            print(" ", end="")
    print()
for _ in range(n + 2):
    print("@", end="")