A, B, C = map(int, input().split(" "))
if (C-B>0) and A>0  : 
    bep = (A // (C-B)) + 1
    print(bep)
else :
    print(-1)