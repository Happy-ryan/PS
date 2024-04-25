n, h = map(int, input().split())
highs = [int(input()) for _ in range(n)]

def solution(n, h, highs):
    nums = [0] * (h)
    for idx, high in enumerate(highs):
        if idx % 2 == 0:
            nums[0] += 1
            nums[high] -= 1
        else:
            nums[h - high] += 1
            
    for i in range(h - 1):
        nums[i + 1] += nums[i]
        
    min_val = min(nums)
    cnt = nums.count(min_val)
        
    return min_val, cnt
    

print(*solution(n, h, highs))