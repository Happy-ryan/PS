while True :
    arr = list(map(int, input().split()))
    if -1 in arr :
        break
    else :
        cnt = 0   
        for j in arr[:len(arr)-1] :
            if j*2 in arr :
                cnt +=1
        print(cnt)