from heapq import heappush, heappop

def solution(M, nums):
    
    # left 작은 수 right 큰 수
    # left의 가장 큰 수가 가운데에 오도록 조정
    # 짝수개(4)일 때 left 2 right2
    # 홀수개(5)일 때 left3 right2
    
    answer = [-1]
    left, right = [],[] # 최대힙, 최소힙
    
    for num in nums:
        
        # 1. 초기 셋팅
        # left right 같다면 left쪽에 
        if len(left) == len(right):
            heappush(left, -num)
        else:
            heappush(right, num)
            
        # 2. 유효성 검사
        # num까지 넣고나서 현재 left와 right가 논리적으로 맞는가 확인
        
        if left and right:
            left_max = -left[0]
            right_min = right[0]
            # left_max < right_min 인 상태가 정상상태
            if left_max > right_min:
                l = -heappop(left)
                r = heappop(right)
                heappush(left, -r)
                heappush(right, l)

        if len(left) != len(right): # 홀수번째에서만 중앙값 판단
            answer.append(-left[0]) 
            
    cnt = len(answer)
    # print(answer)
    print(cnt - 1)
    for i in range(1, cnt):
        print(answer[i], end=' ')
        if i % 10 == 0:
            print()

        

T = int(input())
for _ in range(T):
    M = int(input())
    rows = [list(map(int, input().split())) for _ in range((M // 10) + 1)]
    nums = []
    for row in rows:
        nums.extend(row)
    solution(M, nums)