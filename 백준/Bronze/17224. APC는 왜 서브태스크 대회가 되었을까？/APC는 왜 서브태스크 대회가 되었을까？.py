n, l, k = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(n)]

from heapq import heappush, heappop

def solution(n, l, k, problems):
    heap = []
    
    score = 0
    
    for easy, hard in problems:
        if hard <= l:
            heappush(heap, -140)
        else:
            if easy > l:
                continue
            heappush(heap, -100)
    
    # 점수의 최대를 구해야하므로,, heap이 있는 동안 pop 시킨다.
    for _ in range(k):
        if heap:
            score += heappop(heap)

    return -score


print(solution(n, l,k, problems))  