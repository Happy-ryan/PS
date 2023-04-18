#-2 0 21 3 8 17 32 -8 7 0

arr = list(map(int, input().split()))
cnt = 0
for x in arr:
    if x >0:
        cnt += 1
        
print(cnt)