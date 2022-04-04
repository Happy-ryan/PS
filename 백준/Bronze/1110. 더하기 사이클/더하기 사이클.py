N = int(input())
M = N
cnt = 0
while True :
    arr = list(map(int, str(M)))
    sum_arr =list(map(int,str(sum(arr))))
    result = arr[-1]*10+sum_arr[-1]
    if N == result :
        cnt+=1
        break
    else : 
        if N == result :
            cnt += 1
            break
        else :
            M = result
            cnt +=1

print(cnt)