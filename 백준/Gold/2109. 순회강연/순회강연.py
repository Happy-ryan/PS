n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]

from heapq import heappush, heappop

def solution(n, infos):
    
    # d가 짧은데 p를 많이 받는 곳
    heap = []
    for info in infos:
        p, d = info
        heappush(heap, (d, -p))
    
    selected = []
    
    while heap:
        d, p = heappop(heap)
        p = -p
        # print(f"p: {p}, d: {d}")
        if d > len(selected):
            heappush(selected, p)
        else:
            # 더 좋은 강연으로 최적화 -> 돈 적게 받는 것은 제외.
            min_p = selected[0]
            if min_p < p:
                heappop(selected)
                heappush(selected, p)
                
        # print(selected)

    return sum(selected)

print(solution(n, infos))