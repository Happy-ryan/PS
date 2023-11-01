# https://www.acmicpc.net/problem/1715
# 그리디 유형 - 숫자합치기: 순서에 상관없이 작은 수끼리 먼저 더하면 비용이 최소화가 된다.
from heapq import heappush, heappop

n = int(input())
nums = [int(input()) for _ in range(n)]

heap = []

for num in nums:
    heappush(heap, num)

cost = 0
while len(heap) >= 2:
    x1 = heappop(heap)
    x2 = heappop(heap)
    
    k = x1 + x2
    cost += k
    heappush(heap, k)
    
print(cost)