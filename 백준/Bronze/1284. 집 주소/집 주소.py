while True:
    N = int(input())
    if N == 0:
        break
    else:
        arr = list(str(N))
        cnt = 1 + len(arr)
        for x in arr:
            if int(x) == 1:
                cnt +=2
            elif int(x) == 0:
                cnt +=4
            else:
                cnt +=3
        print(cnt)