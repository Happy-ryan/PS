n = int(input())
nums = [int(input()) for _ in range(n)]

def solution(n, nums):
    
    for num in nums:
        if num < 48:
            return "False"
    
    return "True"

print(solution(n, nums))