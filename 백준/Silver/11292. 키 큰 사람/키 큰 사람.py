while True:
    N = int(input())
    if N == 0:
        break
    else: 
        high=[]
        arr= [ input().split() for _ in range(N)]

        for i in range(N):
            high.append((arr[i][1]))
        max_high = max(high)
        for j in range(N):
            if arr[j][1] == max_high:
                print(arr[j][0],end =" ")