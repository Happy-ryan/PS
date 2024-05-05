from heapq import heappop, heappush

n = int(input())
nums = [int(input()) for _ in range(n)]

def solution(n, nums):
    heap = []
    
    for num in nums:
        heappush(heap, num)
    
    for _ in range(n - 1):
        x1 = heappop(heap)
        x2 = heappop(heap)
        m = (x1 + x2) / 2
        heappush(heap, m)
        
    return f"{heap[0]:.6f}"

print(solution(n, nums))