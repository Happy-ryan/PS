# https://www.acmicpc.net/problem/3040
from itertools import combinations

arr = [int(input()) for _ in range(9)]
ans = []
for x1, x2, x3, x4, x5, x6, x7 in combinations(arr, 7):
    if x1 + x2 + x3 + x4 + x5 + x6 + x7 == 100:
        ans = [x1, x2, x3, x4, x5, x6, x7]
        break
    
for x in ans:
    print(x)