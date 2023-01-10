from heapq import heappush, heappop

def solution(operations):
    answer = []
    erased = [0] * len(operations)
    min_heap = []
    max_heap = []
    
    def pop(heap):
        while heap:
            x, idx = heappop(heap)
            if erased[idx] == 0:
                erased[idx] = 1
                return x, idx
        return 0, -1
    
    for i, row in enumerate(operations):
        op, num = row.split()
        num = int(num)
        
        if op == 'I':
            heappush(min_heap, (num, i))
            heappush(max_heap, (-num, i))
        else:
            if num == 1: # 최댓값 삭제 > max_heap에서 제거
                x, idx = pop(max_heap)
            else:
                x, idx = pop(min_heap)
                
    # 마지막 min과 max 체크하기
    min_num, _ = pop(min_heap)
    max_num, _ = pop(max_heap)
    
    return [-max_num, min_num]
