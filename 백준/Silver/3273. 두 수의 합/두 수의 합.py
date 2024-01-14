# https://www.acmicpc.net/problem/3273

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
x = int(input())

def tow_pointer():
    cnt = 0
    l, r = 0, n - 1
    while l < r:
        k = nums[l] + nums[r]
        if k == x:
            cnt += 1
            k -= nums[l]
            k -= nums[r]
            l += 1
            r -= 1
        elif k > x:
            r -= 1
        elif k < x:
            l += 1
    return cnt

print(tow_pointer())