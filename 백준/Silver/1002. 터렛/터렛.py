from math import *
T = int(input())
for _ in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d1 = (x2-x1)**2
    d2 = (y2-y1)**2
    d = sqrt(d1+d2)
    if d == 0 :
        if r1 == r2 :
            print(-1)
        else :
            print(0)
    else :
        if d > (r1+r2) :
            print(0)
        elif d == (r1 + r2) :
            print(1)
        elif d == abs(r1-r2) :
            print(1)
        elif (0< d) and (d < abs(r1-r2))  :
            print(0)
        else :
            print(2)