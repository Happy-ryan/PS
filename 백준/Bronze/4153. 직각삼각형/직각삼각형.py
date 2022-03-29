from math import *
while True :
    a, b, c = map(int, input().split())
    if (a==0) and (b==0) and (c==0) :
        break
    else :
        case1 = c**2-(a**2+b**2)
        case2 = b**2-(a**2+c**2)
        case3 = a**2-(c**2+b**2)
        if (case1==0) or (case2==0) or (case3==0) :
            print("right")
        else :
            print("wrong") 
        