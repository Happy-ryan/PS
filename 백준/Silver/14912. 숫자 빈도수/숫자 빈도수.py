n,m = map(int,input().split())
cnt =[0 for _ in range(10)]
for x in range(1,n+1):
    arr = list(str(x))
    for i in arr :
        cnt[int(i)] += 1
print(cnt[m])  