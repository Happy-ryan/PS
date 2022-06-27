for _ in range(3):
    arr = list(map(int,input().split()))
    total1 = 0
    total2 = 0
    total1 += arr[0]*60*60
    total1 += arr[1]*60
    total1 += arr[2]
    total2 += arr[3]*60*60
    total2 += arr[4]*60
    total2 += arr[5]
    result = total2 - total1
    h = result//(60*60)
    m = (result-h*3600)//60
    s = result -h*3600 -m*60
    print(h,m,s)