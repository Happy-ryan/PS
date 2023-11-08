# https://www.acmicpc.net/problem/12014

def lengthOfLIS(nums: list[int]):
    from bisect import bisect_left
    
    stack = []
    prev = {}
    
    for i, num in enumerate(nums):
        idx = bisect_left(stack,(num, -1))
        if idx == len(stack):
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

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    nums = list(map(int, input().split()))
    if b > lengthOfLIS(nums):
        print(f"Case #{i + 1}")
        print(0)
    else:
        print(f"Case #{i + 1}")
        print(1)