n = int(input())
nums = list(map(int, input().split()))
x = int(input())

def solution(n, nums, x):
    # 서로 다른 양의 정수 nums
    # 자연수 x = a_i + a_j를 만족하는 쌍의 수
    
    # 순서가 합에 영향을 미치지 않기때문에 정렬하고 시작!
    nums.sort()
    
    # 이중 for문 사용하면 시간초과(n^2)
    # 이분탐색 / 누적합 / 투포인터 등을 이용해서 시간초과를 해결하는게 문제의 포인트!
    # 1 2 3 5 7 9 10 11 12
    
    # 양방향 투포인터
    def two_pointer(n, nums, x):
        cnt = 0
        
        l, r = 0, n - 1
        while l < r and r < n:
            sum_val = nums[l] + nums[r]
            if x < sum_val:
                r -= 1
            elif x > sum_val:
                l += 1
            else:
                cnt += 1
                l += 1
                r -= 1
                
        return cnt
    
    return two_pointer(n, nums, x)

print(solution(n, nums, x))