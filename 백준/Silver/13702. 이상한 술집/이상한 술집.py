# https://www.acmicpc.net/problem/13702

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def binary_search():
    l, r = 0, 2**31
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if get(arr, m) >= k:
            l = m + 1
            ans = m
        else:
            r = m - 1
    return ans
    

def get(arr, m):
    cnt = 0
    for x in arr:
        cnt += x // m
    return cnt

print(binary_search())