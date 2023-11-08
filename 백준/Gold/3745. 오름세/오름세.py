# https://www.acmicpc.net/problem/3745

def lengthOfLIS(nums: list[int]):
    from bisect import bisect_left
    stack = []
    prev = {}
    
    for i, num in enumerate(nums):
        idx = bisect_left(stack, (num, -1))
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
        
    return len(ans)

while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        print(lengthOfLIS(nums))
    except EOFError:
        break