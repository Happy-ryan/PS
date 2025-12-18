t = int(input())

def solution(r1, c1, r2, c2):
    R = abs(r1 - r2)
    C = abs(c1 - c2)
    
    if (R == 1 and C == 2) or (R == 2 and C == 1):
        return 'YES'
    return 'NO'

for i in range(1, t + 1):
    n, r1, c1, r2, c2 = map(int, input().split())
    print(f"Case {i}: {solution(r1, c1, r2, c2)}")
