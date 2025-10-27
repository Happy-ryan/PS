T = int(input())

for _ in range(T):
    
    d, n, s, p = map(int, input().split())
    
    S = n * s
    P = d + n * p

    if S < P:
        print("do not parallelize")
    elif S > P:
        print("parallelize")
    else:
        print("does not matter")
