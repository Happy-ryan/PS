N = int(input())
arr=list(map(int,input().split()))
M = int(input())
qs = list(map(int, input().split()))

arr = sorted(arr)


def lower_bound(arr,x) :
    l, r = -1,len(arr)
    while r-l != 1 :
        m = (l+r) //2 
        if x > arr[m] :
            l = m
        else :
            r = m  
    return r
def upper_bound(arr,x) :
    l, r = -1, len(arr)  # r의 범위가 0~5 이므로 l의 범위는 0~4
    while r - l != 1 :
        m = (r+l)//2
        if x >= arr[m] :
            l = m
        else :
            r = m 
    return r

for x in qs :
    idx = lower_bound(arr,x)
    if idx < len(arr) and arr[idx] == x :
        print(upper_bound(arr,x)-lower_bound(arr,x))
    else :
        print(0)