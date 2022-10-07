k,w,m = map(int,input().split())
i = 0
while True:
    if k >= w:
        print(i)
        break
    else:
        k += m
        i += 1