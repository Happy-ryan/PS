n = int(input())

if n == 1 :
    print("1/1")
else :
    num = 2
    cnt = 2
    while True  :
        if (num <= n) and (n<=num+(cnt-1)) :
            break
        else :
            num = num + cnt
            cnt +=1
    i = n - num
    a = cnt - i
    b = 1 + i
    if cnt%2 !=0 :
        print(f"{a}/{b}")
    else :
        print(f"{b}/{a}")