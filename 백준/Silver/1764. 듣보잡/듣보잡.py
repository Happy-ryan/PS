N,M = map(int, input().split())
arr = [ input() for _ in range(N)]
brr = [ input() for _ in range(M)]
qs = sorted(arr+brr)
result=[]
cnt = 0
for i in range(len(qs)-1):
    if qs[i] == qs[i+1]:
        cnt +=1
        result.append(qs[i+1])
print(cnt)
print(*result,sep="\n")