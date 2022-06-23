n = int(input())
arr = list(map(int,input().split()))
arr.append(0)
arr.sort()
brr = set(arr)
k = int(input())
if k in brr:
    print(0)
else:
    for i in range(len(arr)-1):
        row = list(range(arr[i]+1,arr[i+1]))
        if k not in row:
            continue
        else:
            idx = row.index(k)
            result = (len(row)-(idx+1)) + idx*(len(row)-idx)
            print(result)
            break
# https://www.acmicpc.net/problem/1059