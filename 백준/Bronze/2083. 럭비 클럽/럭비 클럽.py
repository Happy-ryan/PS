while True:
    arr = list(input().split())
    # arr =[[a,int(b),int(c)] for a,b,c in arr]
    if arr[0] =='#':
        break
    else:
        if int(arr[1]) >17 or int(arr[2]) >= 80:
            print(arr[0],'Senior')
        else:
            print(arr[0],'Junior')