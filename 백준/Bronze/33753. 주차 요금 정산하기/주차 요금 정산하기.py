from math import ceil

A, B, C = map(int, input().split())
T = int(input())

if T <= 30:
    print(A)
else:
    print(A + ceil((T - 30) / B) * C)