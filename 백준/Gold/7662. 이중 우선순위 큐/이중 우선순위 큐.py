import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    Q = int(input())
    operations = []
    for _ in range(Q):
        operations.append(input())

    def solution(operations):
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
                    
        # min과 max 마지막 체크하기 min_heap = [], max_heap = [(123,2)], erased[2] = 1 상황 
        min_num, min_idx = pop(min_heap)

        if min_idx != -1:
            erased[min_idx] = 0

        max_num, max_idx = pop(max_heap)
 

        if min_idx == -1 and max_idx == -1:
            return "EMPTY"
        else:
            return f"{-max_num} {min_num}"

    print(solution(operations))