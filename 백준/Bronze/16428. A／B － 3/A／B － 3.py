A, B = map(int, input().split())

def solution(A, B):
    
    if A == 0:
        print(0)
        print(0)
        return

    if B < 0:
        q = -(A // abs(B))
    elif A < 0:
        q = -((abs(A) // B) + 1)
    else:
        q = A // B
        
    
    r = A - q * B
    
    print(q)
    print(r)
    return

solution(A, B)