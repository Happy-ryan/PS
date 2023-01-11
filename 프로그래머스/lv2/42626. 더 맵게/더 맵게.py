from heapq import heappop, heappush

def solution(scoville, K):
    answer = 0
    min_heap = []
    for x in scoville:
        heappush(min_heap, x)
        
    while True:
        if len(min_heap) == 1: #min_heap 1개 남으면 이건 종료조건과 동일함
            last = heappop(min_heap)
            if last >= K:
                return answer
            else:
                return -1
        else:
            x1 = heappop(min_heap)
            x2 = heappop(min_heap)
            if x1 >= K: # min_heap의 최솟값을 의미
                return answer
            else:
                x3 =  x1 + 2 * x2
                heappush(min_heap, x3)
                answer += 1
        
            
