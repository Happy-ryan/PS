while True:
    arr = list(input().split())
    if arr[-1] =='#':
        break
    else:
        cnt = 0
        for i in range(1,len(arr)):
            row = arr[i]
            row = row.lower()
            for x in row:
                if x == arr[0]:
                    cnt +=1
        print(arr[0],cnt)