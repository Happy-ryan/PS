from heapq import heappop, heappush

N = int(input())
nums = [int(input()) for _ in range(N)]

def solution(N, nums):
    
    min_heap = []
    max_heap = []
    
    for num in nums:
        if num == 0:
            if not max_heap:
                print(0)
            else:
                print(-heappop(max_heap))
        else:
            heappush(max_heap, -num)
    
solution(N, nums)