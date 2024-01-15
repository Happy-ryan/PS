n = int(input())
nums = list(map(int, input().split()))
nums.sort()

def two_pointer():
    ans = 2000000000
    position = [0, n - 1]
    l, r = 0, len(nums) - 1
    while l < r:
        sum_val = nums[l] + nums[r]
        if ans >= abs(sum_val):
            ans = abs(sum_val)
            position[0] = l
            position[1] = r

        if sum_val < 0:
            l += 1
        else: 
            r -= 1
    
    return nums[position[0]], nums[position[1]]

print(*two_pointer())