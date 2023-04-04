n = int(input())
cnt = 0
for b in range(1, 501):
    for a in range(b,501):
        if a ** 2 == n + b ** 2:
            cnt += 1
print(cnt)