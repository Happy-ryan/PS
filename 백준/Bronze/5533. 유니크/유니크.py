# https://www.acmicpc.net/problem/5533
from collections import Counter

n = int(input())
board = [ list(map(int, input().split())) for row in range(n)]
score = [0] * n

board_change = []
for c in range(3):
    row = []
    for r in range(n):
        row.append(board[r][c])
    board_change.append(row)
    
# 시간복잡도 충분함.  
for row in board_change:
    dic = Counter(row)
    for i, x in enumerate(row):
        if dic[x] >= 2:
            row[i] = 0
            
for c in range(n):
    total = 0
    for r in range(3):
        total += board_change[r][c]
    print(total)