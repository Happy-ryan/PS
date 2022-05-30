day = int(input())
arr = list(map(int,input().split()))
cnt = 0
for x in arr:
    if x == day:
        cnt +=1
print(cnt)
