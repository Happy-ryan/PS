# https://www.acmicpc.net/problem/3273

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
x = int(input())

def tow_pointer():
    cnt = 0
    l, r = 0, n - 1
    k = nums[l] + nums[r]
    while l < r:
        if k <= x:
            if k == x:
                cnt += 1
            k -= nums[l]
            l += 1
            k += nums[l]
        elif k > x:
            k -= nums[r]
            r -= 1
            k += nums[r]

    return cnt

print(tow_pointer())
