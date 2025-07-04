while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    n = 1
    for i in range(arr[0]):
        s1 = arr[2 * i + 1]
        s2 = arr[2 * i + 2]
        n *= s1
        n -= s2
        
    print(n)