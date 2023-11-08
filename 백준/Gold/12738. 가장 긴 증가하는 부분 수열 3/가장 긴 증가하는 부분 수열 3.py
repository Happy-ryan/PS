from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))

stack = []
prev = {}

for i, num in enumerate(nums):
    idx = bisect_left(stack, (num, -1))
    if idx == len(stack):
        stack.append((num, i))
    else:
        stack[idx] = (num, i)
    if idx > 0:
        prev[i] = stack[idx - 1]
    
print(len(stack))

# cur 인덱스 / ans 값
# cur = stack[-1][1]
# ans = [stack[-1][0]]
# while cur in prev:
#     cur = prev[cur][1]
#     ans.append(nums[cur])
    
# print(len(ans[::-1]))