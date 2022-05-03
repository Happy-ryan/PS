N = int(input())
arr = list(map(int, input().split()))
M = int(input())
qs = list(map(int, input().split()))

arr = sorted(arr)

def lower_bound(arr,x) : # arr에서 x를 찾는 함수
    l,r = -1, len(arr)
    while r-l != 1 :
        m = (r+l)//2
        if x < arr[m] :
             r = m 
        else:
            l = m 
    return l

for x in qs :
    idx = lower_bound(arr,x)
    if idx < len(arr) and arr[idx] == x :
        print(1)
    else :
        print(0)