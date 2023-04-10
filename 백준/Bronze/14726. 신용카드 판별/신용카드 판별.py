# # https://www.acmicpc.net/problem/14726


def f(arr):
    arr = arr[::-1]
    ans = 0
    for i, x in enumerate(arr): #i : int / x :str
        if i % 2 == 0: # 홀수번째
            ans += int(x)
        else: #짝수번째
            k = 2 * int(x)
            sum_val = 0
            if k >= 10:
                sum_val += k // 10
                sum_val += k % 10 
                k = sum_val
            ans += k
    
    if ans % 10 == 0:
        return "T"
    else:
        return "F"
    

t = int(input())
for _ in range(t):
    arr = list(str(input()))
    print(f(arr))
