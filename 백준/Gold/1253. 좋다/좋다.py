# n개의 수 중 어떤 수가 다른 수 두개의 합으로 = 좋다
# n개의 수가 주어지면 그 중에서 좋은 수의 개수

n = int(input())
nums = list(map(int, input().split()))

def solution(n, nums):
    # 정렬해도 문제 없어 보임
    nums.sort()
    
    def two_pointer(nums, target):
        # l, r 모두 움직임 / 다른 방향
        # 둘 다 고정아님. 왜 고정을 안할까?
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
    
    def do_pointer(nums, target):
        # l이동 / r고정
        l = 0
        for r in range(len(nums) - 1, -1, -1):
            # l과 r이 절대로 같아져서는 안돼.
            if l == r:
                return 0
            while l + 1 < r and nums[l] + nums[r] < target:
                l += 1
            
            if nums[l] + nums[r] == target:
                # print(f"l: {l}, r: {r}, {nums[l]} + {nums[r]} = {target}")
                return 1
        
        return 0
    
    # 투 포인터(n) * n번 돌림.
    # idx의 숫자를 그 숫자를 제외한 나머지로 만들 수 있는가를 확인
    # 해당 idx를 빼기 위해서 nums를 재편함. 
    ans = 0
    for idx in range(n):
        # ans += two_pointer(nums[:idx] + nums[idx + 1:], nums[idx]) # idx 숫자를 만들 수 있는지 찾기
        ans += do_pointer(nums[:idx] + nums[idx + 1:], nums[idx]) # idx 숫자를 만들 수 있는지 찾기

    return ans
    
print(solution(n, nums))