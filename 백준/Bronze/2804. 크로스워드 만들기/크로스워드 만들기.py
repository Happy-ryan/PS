# https://www.acmicpc.net/problem/2804
from pprint import pprint

sa, sb = input().split()

def f(sa, sb):
    for a in range(len(sa)):
        for b in range(len(sb)):
            if sa[a] == sb[b]:
                board_col = a
                board_row = b
                return board_col, board_row
    
board = [["." for col in range(len(sa))] for row in range(len(sb))]

# print(f(sa, sb))
for col in range(len(sa)):
    board[f(sa, sb)[1]][col] = sa[col]
    
for row in range(len(sb)):
    board[row][f(sa, sb)[0]] = sb[row] 
    
for row in board:
    print(''.join(row))