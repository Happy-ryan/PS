from heapq import heappush, heappop

def solution(N, nums):
    left = []   # 최대 힙 (음수로 저장)
    right = []  # 최소 힙
    
    answer = []
    
    for num in nums:
        # 1. 새 숫자를 적절한 힙에 추가
        if len(left) == len(right):
            heappush(left, -num)
        else:
            heappush(right, num)
        
        # 2. 두 힙의 값 규칙 유지 (left의 최댓값 ≤ right의 최솟값)
        if left and right and -left[0] > right[0]:
            left_max = -heappop(left)
            right_min = heappop(right)
            heappush(left, -right_min)
            heappush(right, left_max)
        
        # 3. 중간값 출력 (항상 left의 top)
        answer.append(-left[0])
    
    for x in answer:
        print(x)

N = int(input())
nums = [int(input()) for _ in range(N)]
solution(N, nums)