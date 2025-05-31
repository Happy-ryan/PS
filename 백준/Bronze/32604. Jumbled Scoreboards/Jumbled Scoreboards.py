n = int(input())

nt, np = -1, -1
flag = True


for _ in range(n):
    a, b = map(int, input().split())

    if not flag:
        continue

    if nt > a or np > b:
        flag = False
        continue

    nt, np = a, b

print('yes' if flag else 'no')