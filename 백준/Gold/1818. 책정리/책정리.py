# https://www.acmicpc.net/problem/1818
# 1 ~ N : LIS = N

# LIS : 1 -> 4번
# 5 4 3 2 1 
# 5 4 3 1 2
# 5 4 1 2 3
# 5 1 2 3 4
# 1 2 3 4 5

# LIS : 4 -> 1번
# 1 5 2 3 4
# 1 2 3 4 5

# LIS : 3 -> 2번
# 3 4 1 5 2
# 1 3 4 5 2
# 1 2 3 4 5

# LIS : 2 -> 3번
# 3 5 2 1 4
# 2 3 5 1 4
# 1 2 3 5 4
# 1 2 3 4 5

# 유형1. 전깃줄 .. 선이 안꼬이게
# 유형2. 정렬을 위해서 최소 몇 번의 이동?

from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))

stack = []
prev = {}

for i, num in enumerate(nums):
    idx = bisect_left(stack,(num, -1))
    if len(stack) == idx:
        stack.append((num, i))
    else:
        stack[idx] = (num, i)
    if idx > 0:
        prev[i] = stack[idx - 1]
        
cur = stack[-1][1]
ans = [stack[-1][0]]

while cur in prev:
    cur = prev[cur][1]
    ans.append(nums[cur])
    
print(n - len(stack))
# print(n - len(ans))