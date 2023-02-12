from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    min_heap = []
    max_heap = []
    for x in arr:
        heappush(min_heap, x)
        heappush(max_heap, -x)
    print(heappop(min_heap), -heappop(max_heap))
