import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
min_heap = []
erased = [0] * n

def pop(heap):
    while heap:
        x, idx = heappop(heap)
        if erased[idx] == 0:
            erased[idx] = 1
            return x, idx
    return 0, -1 # 힙이 비어있을 때

for i in range(n):
    num = int(input())
    if num == 0:
        x, idx = pop(min_heap)
        print(x)
    else:
        heappush(min_heap, (num, i))
