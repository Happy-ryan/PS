import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())
board = [ list(map(int, input().split())) for row in range(n)]
max_heap = []
min_heap = []
cnt = 0
for c in range(n):
        heappush(min_heap, board[0][c])

for r in range(1, n):
    for c in range(n):
        heappush(min_heap, board[r][c])
        heappop(min_heap)

print(sorted(min_heap)[0])