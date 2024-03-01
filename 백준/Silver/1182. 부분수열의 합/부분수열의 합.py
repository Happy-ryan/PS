n, s = map(int, input().split())
nums = list(map(int, input().split()))

def solution(n, s, nums):
    
    sum_val = 0
    cnt = 0
    def dfs(idx):
        nonlocal cnt, sum_val
        if idx == n:
            if sum_val == s:
                cnt += 1
            return
        
        # 선택했다.
        sum_val += nums[idx]
        dfs(idx + 1)
        sum_val -= nums[idx]
        
        # 선택 안했다.
        dfs(idx + 1)
    
    dfs(0)
    
    # 공집합!!
    if s == 0:
        cnt -= 1
    return cnt

print(solution(n, s, nums))