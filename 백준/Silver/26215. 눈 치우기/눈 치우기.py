n = int(input())
snows = list(map(int, input().split()))

from heapq import heappop, heappush

def solution(n, snows):
    
    heap = []
    for snow in snows:
        heappush(heap, -snow)
    t = 0
    while heap:
        if len(heap) >= 2:
            s1 = -heappop(heap)
            s2 = -heappop(heap)
            
            s1 -= 1
            s2 -= 1
            if s1 > 0:
                heappush(heap, -s1)
            if s2 > 0:
                heappush(heap, -s2)
        else:
            s1 = -heappop(heap)
            s1 -= 1
            if s1 > 0:
                heappush(heap, -s1)
        t += 1
        # print(f"시간: {t} / 눈 상태: {heap}")

    if t > 1440:
        return -1
    return t
        

print(solution(n, snows))