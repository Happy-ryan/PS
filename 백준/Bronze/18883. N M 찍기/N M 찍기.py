n, m = map(int, input().split())
k = 1
for _ in range(n):
    row = ""
    for _ in range(m):
        row += str(k) + " "
        k += 1
    print(row[:-1])