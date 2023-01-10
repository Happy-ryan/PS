
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
# 파이썬 디폴트 : min_heap
# max_heap은 minus를 활용
n = int(input())
max_heap = []
erased = [0] * n

def pop(heap):
    while heap:
        x, idx = heappop(heap)
        if erased[idx] == 0:
            erased[idx] = 1
            return x, idx
    return 0, -1

for i in range(n):
    num = int(input())
    if num == 0:
        x, idx = pop(max_heap)
        print(-x)
    else:
        heappush(max_heap, (-num, i))
