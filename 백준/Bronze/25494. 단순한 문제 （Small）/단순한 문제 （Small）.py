T = int(input())

def f(a,b,c):
    s = 0
    for x in range(1,a+1):
        for y in range(1,b+1):
            for z in range(1,c+1):
                if (x%y == y%z) and (x%y == z%x) and (y%z == z%x):
                    s += 1
    return s
    
for _ in range(T):
    a,b,c = map(int,input().split())
    print(f(a,b,c))