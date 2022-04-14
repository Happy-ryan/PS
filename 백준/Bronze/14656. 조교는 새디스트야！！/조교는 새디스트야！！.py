N = int(input())
arr=list(map(int, input().split()))
cnt = 0
brr = sorted(arr)
for i in range(N) :
    if arr[i] != brr[i] :
        cnt +=1
print(cnt)