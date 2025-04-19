# n개의 수 중 어떤 수가 다른 수 두개의 합으로 = 좋다
# n개의 수가 주어지면 그 중에서 좋은 수의 개수

n = int(input())
nums = list(map(int, input().split()))

def solution(n, nums):
    # 정렬해도 문제 없어 보임
    nums.sort()
    
    def two_pointer(nums, target):
        # l, r 모두 움직임 / 다른 방향
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                return 1
        return 0

    ans = 0
    for idx in range(n):
        ans += two_pointer(nums[:idx] + nums[idx + 1:], nums[idx]) # idx 숫자를 만들 수 있는지 찾기
        
    return ans
    
print(solution(n, nums))