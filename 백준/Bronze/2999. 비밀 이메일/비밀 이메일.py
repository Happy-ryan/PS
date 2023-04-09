# https://www.acmicpc.net/problem/2999
from typing import List, Tuple

def GetDivosr(arr:List) -> Tuple:
    ans = 0
    n = len(arr)
    for r in range(1, int(n**(0.5)) + 1):
        c = n // r
        if r <= c and r * c == n:
            ans = max(ans, r)
        
    return (ans, n//ans)


def board(r:int, c:int, arr:List):
    board_2d = [
        [0 for col in range(c)]
        for row in range(r)
    ]
    
    p = 0
    for j in range(c):
        for i in range(r):
            board_2d[i][j] = arr[p]
            p += 1
    
    ans = ""
    for row in board_2d:
        ans += "".join(row)
        
    return ans

arr = input()
r, c = GetDivosr(arr)
print(board(r, c, arr))