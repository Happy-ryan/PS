# https://www.acmicpc.net/problem/5235
def f(arr: list):
    arr = arr[1:]
    sum_even = 0
    sum_odd = 0
    for idx, x in enumerate(arr):
        if x % 2 == 0:
            sum_even += x
        else:
            sum_odd += x
    
    if sum_even > sum_odd:
        return "EVEN"
    elif sum_even < sum_odd:
        return "ODD"
    else:
        return "TIE"
        
t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    print(f(arr))