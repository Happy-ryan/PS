n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
cnt = 0
for row in arr:
    if row.count("O") * 2 > m:
        cnt += 1
print(cnt)