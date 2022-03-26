n = int(input())
if n == 1 :
    print(1)
else :
    cnt = 2
    num =2
    while True :
        if  (cnt<= n) and (n < cnt+6*(num-1)) :
            break
        else :
            cnt += 6*(num-1)
            num += 1
    print(num)
