t = int(input())

from heapq import heappop, heappush

def solution(k, files):
    sum_val = 0
    heap = []
    for file in files:
        heappush(heap, file)

    def pick():
        res = 0
        while heap:
            if len(heap) == 1:
                return res
            f1 = heappop(heap)
            f2 = heappop(heap)
            res += (f1 + f2)
            heappush(heap, f1 + f2)
            # print(heap)

    sum_val = pick()
    
    return sum_val
    
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    print(solution(k, files))