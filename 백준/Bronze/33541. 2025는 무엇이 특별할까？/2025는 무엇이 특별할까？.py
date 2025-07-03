x = int(input())

def solution(x):

    for p in range(x + 1, 10000):
        p1 = p // 100
        p2 = p % 100
        
        if (p1 + p2) ** 2 == p:
            return p
    
    return -1

print(solution(x))