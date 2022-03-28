M = int(input())
N = int(input())
arr=[]
for i in range(M, N+1) :
    for j in range(2, N+1) :
        if (i % j == 0) and i != j :
            break
        elif i%j != 0 :
            pass
        elif (i%j == 0) and (i ==j) :
            arr.append(j)
if arr == [] :
    print(-1)
else :
    sum = 0
    for k in arr :
        sum += k
    print(sum)
    print(arr[0])