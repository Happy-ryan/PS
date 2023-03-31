# https://www.acmicpc.net/problem/2615
from itertools import combinations


def check(arr2d_1, arr2d_2):
    cnt = 0
    for r in range(len(arr2d_1)):
        for c in range(len(arr2d_1[0])):
            if arr2d_1[r][c] != arr2d_2[r][c]:
                cnt += 1
    return cnt

n = int(input())
board = []

for _ in range(n):
    
    arr2d = [
        list(input())
        for row in range(5)
    ]
    
    board.append(arr2d)
    
    
ans = []
for x1, x2 in combinations(list(range(n)), 2):
    ans.append((check(board[x1], board[x2]), x1 + 1, x2 + 1))
    
ans.sort(key=lambda x: x[0])
ans = sorted([ans[0][1], ans[0][2]])
print(*ans)

