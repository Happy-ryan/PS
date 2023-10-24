# https://www.acmicpc.net/problem/12015
# 시간복잡도 O(N^2) > O(NlogN)
from bisect import bisect_left, bisect_right
n = int(input())
nums = list(map(int, input().split()))

stack = [nums[0]]
for num in nums[1:]:
    if stack[-1] < num:
        stack.append(num)
    else:
        idx_left = bisect_left(stack, num)
        # idx_right = bisect_right(stack, num)
        stack[idx_left] = num
        # print(f"stack은 {stack}")
        # print(f"{num}의 idx_left {idx_left}")
        # print(f"{num}의 idx_right {idx_right}")

print(len(stack))