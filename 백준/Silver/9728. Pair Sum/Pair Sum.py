def tow_pointer(nums, m):
    l, r = 0, len(nums) - 1
    k = nums[l] + nums[r]
    cnt = 0
    while l < r:
        if k <= m:
            if k == m:
                cnt += 1
            k -= nums[l]
            l += 1
            k += nums[l]
        else:
            k -= nums[r]
            r -= 1
            k += nums[r]
    return cnt

t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(f"Case #{i}: {tow_pointer(numbers, m)}")