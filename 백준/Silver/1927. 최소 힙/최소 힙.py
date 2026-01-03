from heapq import heappop, heappush

N = int(input())
nums = [int(input()) for _ in range(N)]

def solution(N, nums):
    
    min_heap = []
    
    for num in nums:
        if num == 0:
            if not min_heap:
                print(0)
            else:
                print(heappop(min_heap))
        else:
            heappush(min_heap, num)
    
solution(N, nums)