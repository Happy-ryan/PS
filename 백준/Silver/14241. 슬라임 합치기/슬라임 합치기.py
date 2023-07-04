# https://www.acmicpc.net/problem/14241

from collections import deque

n = int(input())
nums = deque(reversed(sorted(list(map(int, input().split())))))
sum_val = 0
idx = 0
while len(nums) != 1:
    sum_val += nums[idx] * nums[idx + 1]
    new_num = nums[idx] + nums[idx + 1]
    nums.popleft()
    nums.popleft()
    nums.appendleft(new_num)
    
print(sum_val)