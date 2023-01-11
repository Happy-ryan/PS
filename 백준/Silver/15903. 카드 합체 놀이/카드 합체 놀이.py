
import sys
from heapq import heappush, heappop

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# 합의 최솟값 = 가장 작은 값 2개 뽑아서 더해야함.
min_heap = []

for num in numbers:
    heappush(min_heap, num)

for _ in range(m):
    x1 = heappop(min_heap)
    x2 = heappop(min_heap)
    x3 = x1 + x2
    heappush(min_heap, x3)
    heappush(min_heap, x3)

print(sum(min_heap))