n, m = map(int, input().split())
flag = True

for _ in range(n):
    arr = list(input().split())

    if arr.count('A') != 1:
        flag = False

print('Yes' if flag else 'No')