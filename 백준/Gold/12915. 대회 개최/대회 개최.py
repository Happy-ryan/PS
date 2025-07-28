nums = list(map(int, input().split()))

def solution(nums):
    # 쉬운 1 중간 1 어려운 1 <- 대회 기본 셋팅
    
    # 쉬운 문제 후보 = E + EM = 4
    # 중간 문제 후보 = EM + MH +M = 5 
    # 어려운 문제 후보 = MH + H = 4
    
    # 가장 많은 대회가 열릴려면 쉬운문제, 중간문제, 어려운문제가 동일하게 있을 때이다..
    # EM MH는 해당값들을 조정하기 위한 것들
    # EM MH를 얼마나 줘야할지 애매...
    
    # 애매한건 생각말고 고정할 수 있는게 뭐가 있지? 바로 대회횟수!
    
    def open():
        nums[0] -= 1
        nums[2] -= 1
        nums[4] -= 1
        
    def adjust():
        if nums[0] == 0 and nums[1] > 0:
            nums[0] += 1
            nums[1] -= 1
            
        if nums[4] == 0 and nums[3] > 0:
            nums[4] += 1
            nums[3] -= 1
            
        if nums[2] == 0 and (nums[1] > 0 or nums[3] > 0):
            if nums[1] > nums[3]:
                nums[2] += 1
                nums[1] -= 1
            elif nums[1] < nums[3]:
                nums[2] += 1
                nums[3] -= 1
            else:
                if nums[0] > nums[4]:
                    nums[2] += 1
                    nums[1] -= 1
                elif nums[0] <= nums[4]:
                    nums[2] += 1
                    nums[3] -= 1
    
    
    # print("최초: ", nums)
    adjust()
    # print(f"개최 전 조정: ", nums)
    cnt = 0
    i = 0
    while True:
        if nums[0] > 0 and nums[2] > 0 and nums[4] > 0:
            cnt += 1
        open()
        # print(f"{i + 1}회 개최 후 상태: ", nums)
        adjust()
        # print(f"{i + 1}회 개최 후 조정: ", nums)
        if nums[0] <= 0 or nums[2] <= 0 or nums[4] <= 0:
            break
        i += 1
    
    return cnt
        
print(solution(nums))