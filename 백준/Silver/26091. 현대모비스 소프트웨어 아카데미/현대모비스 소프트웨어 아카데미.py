n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 팀원은 반드시 두 명! / 두 명의 합산이 m 이상이어야함
def solution(n, m, nums):
    # 딱히 정렬해도 상관없으면 반드시 정렬하기!
    nums.sort()
    cnt = 0
    l = 0 # <- 움직이는 아이
    # 큰 수를 먼저 선택해서 생각하자.. <- 고정
    # 뒤에서부터 보는게 낫다.
    for r in range(n - 1, 0, -1):
        while l < r and nums[l] + nums[r] < m:
            l += 1
            
        if l < r and nums[l] + nums[r] >= m:
            cnt += 1
            l += 1
    
    return cnt

print(solution(n, m, nums))