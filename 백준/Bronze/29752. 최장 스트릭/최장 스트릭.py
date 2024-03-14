n = int(input())
arr = list(map(int, input().split()))

cnt = 0
max_val = 0
for x in arr:
    if x != 0:
        cnt += 1
    else:
        max_val = max(max_val, cnt)
        cnt = 0
max_val = max(max_val, cnt)
print(max_val)