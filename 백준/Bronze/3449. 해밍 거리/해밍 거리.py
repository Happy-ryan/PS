T = int(input())
for _ in range(T):
    arr = list(input())
    brr = list(input())
    # print(arr)
    # print(brr)
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != brr[i]:
            cnt += 1
    print("Hamming distance is"+' '+str(cnt)+'.') 