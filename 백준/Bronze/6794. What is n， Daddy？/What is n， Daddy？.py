n = int(input())

cnt = 0

for i in range(6):
    for j in range(1, 6):
        if i <= j and i + j == n:
            cnt += 1

print(cnt)