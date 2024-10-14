n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

from math import ceil

def solution(n, sizes, t, p):
    shirt_cnt, pen_cnt = 0, 0
    for size in sizes:
        shirt_cnt += ceil(size / t)
            
    pen_cnt += n // p
        
    print(shirt_cnt)
    print(pen_cnt, n % p)

solution(n, sizes, t, p)