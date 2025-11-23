t = int(input())

def solution(n, nums):
    
    dp = [0] * (n)
    # dp[n] = dp[n - 1] + dp[n - 2]
    dp[0] = nums[0]
    dp[1] = nums[1]
    if n >= 2:
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
    for i in range(n):
        if dp[i] != nums[i]:
            return 'NO'
    return 'YES'
    
for _ in range(t):
    arr = list(map(int, input().split()))
    n, nums = arr[0], arr[1:]
    print(solution(n, nums))