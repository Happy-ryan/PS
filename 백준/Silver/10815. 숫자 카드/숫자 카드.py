N = int(input())
arr = list(map(int, input().split()))
M = int(input())
qs = list(map(int, input().split()))

arr = sorted(arr)
def upper_bound(arr,x) : # upper_bound 구현 = bisect_right()
    l, r = -1, len(arr)  
    while r - l != 1 :
        m = (r+l)//2
        if x >= arr[m] : # upper와 lower 가르는 곳 "="의 차이
            l = m
        else :
            r = m 
    return r

for x in qs :
    idx = upper_bound(arr,x) 
    if arr[idx-1] == x  :
        print(1,end=" ")
    else :
        print(0,end=" ")
