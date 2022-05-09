T = int(input())
arr=[ input().split() for _ in range(T)]

ret1 = arr[0] #part1 나이 적은 사람 찾기
for i in range(1,T):
    x = arr[i]
    if int(x[3]) > int(ret1[3]):
        ret1,x=x,ret1
    elif int(x[3]) == int(ret1[3]):
        if int(x[2]) > int(ret1[2]):
            ret1,x=x,ret1
        elif int(x[2])==int(ret1[2]):
            if int(x[1]) > int(ret1[1]):
                ret1,x=x,ret1
print(ret1[0])
ret2 = arr[0] #part1 나이 많은 사람 찾기
for i in range(1,T):
    x = arr[i]
    if int(x[3]) < int(ret2[3]):
        ret2,x=x,ret2
    elif int(x[3]) == int(ret2[3]):
        if int(x[2]) < int(ret2[2]):
            ret2,x=x,ret2
        elif int(x[2])==int(ret2[2]):
            if int(x[1]) < int(ret2[1]):
                ret2,x=x,ret2
print(ret2[0])