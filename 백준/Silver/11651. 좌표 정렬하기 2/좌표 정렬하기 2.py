N = int(input())
arr = [input().split() for _ in range(N)]
arr = [[int(a), int(b)] for a,b in arr]
result=[]
for i in range(N):
    arr[i][1],arr[i][0] = arr[i][0],arr[i][1]
for i in range(N):
    result.append(tuple(arr[i]))
result = sorted(result)
for row in result:
    crr=list(row)
    crr[0],crr[1]=crr[1],crr[0]
    print(*crr)
