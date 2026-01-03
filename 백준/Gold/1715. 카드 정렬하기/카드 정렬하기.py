N = int(input())
cards = [int(input()) for _ in range(N)]

from heapq import heappop, heappush
def solution(N, cards):
    cards.sort()
    
    heap = []
    
    for card in cards:
        heappush(heap, card)
        
    # print(heap)
    cnt = 0
    while len(heap) > 1:
        # print(f"heap : {heap}")
        a = heappop(heap)
        b = heappop(heap)
        cnt += (a + b)
        heappush(heap, a + b)
        
    return cnt

print(solution(N, cards))