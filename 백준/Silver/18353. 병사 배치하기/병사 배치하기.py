n = int(input())
nums = list(map(int, input().split()))
dp = [-1 for _ in range(n)]

# dpf(x) = max(ret, dpf(i)) + 1 where 0 <= i < x and nums[i] > nums[x]
def dpf(x):
    if dp[x] != -1:
        return dp[x]
    
    ret = 1
    for i in range(0, x):
        if nums[i] > nums[x]:
            ret = max(ret, dpf(i) + 1)
            
    dp[x] = ret
    
    return ret


max_ans = 0
for i in range(n):
    max_ans = max(max_ans, dpf(i))
    
print(n - max_ans)