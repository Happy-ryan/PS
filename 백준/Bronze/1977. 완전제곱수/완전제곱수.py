from math import *
M = int(input())
N = int(input())
arr =[]
a = ceil(sqrt(M))
b = floor(sqrt(N+1))
if (M == N) and ceil(sqrt(M)) == floor(sqrt(N)) :
    print(M)
    print(M)
elif (M==N) and ceil(sqrt(M)) != floor(sqrt(N)) :
    print(-1)
else :
    for x in range(ceil(sqrt(M)), floor(sqrt(N+1))+1) :
        if (M <= x**2) and (x**2 <= N) :
            arr.append(x**2)
    if arr==[] : # 오류가 빈칸이 있어서min을 못한다고 하면 min 나올 때를 조건문으로 하는 센스를 가지자
        print(-1)
    else:
        #print(arr)
        print(sum(arr))
        print(min(arr))