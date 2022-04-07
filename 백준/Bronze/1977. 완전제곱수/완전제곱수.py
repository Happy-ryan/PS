from math import *
M = int(input())
N = int(input())
arr =[]
a = ceil(sqrt(M))
b = floor(sqrt(N+1))
for x in range(1, 101) : #N의 범위가 10000이하이므로 전수를 돌릴 수 있다.
    if (M <= x**2) and (x**2<=N) :
        arr.append(x**2)
if len(arr)==0 :
    print(-1)
else :
    print(sum(arr))
    print(min(arr))