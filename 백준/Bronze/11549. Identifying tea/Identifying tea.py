T = int(input())
arr = list(map(int,input().split()))

cnt = 0
for x in arr:
    if T == x:
        cnt += 1

print(cnt)