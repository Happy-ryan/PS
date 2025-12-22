while True:
    N, M = map(int, input().split())
    
    if N == 0 and M == 0:
        break
        
    A = list(map(int, input().split()))

    total = 0
    fee = M // N
    for a in A:
        total += min(fee, a)
        
    print(total)