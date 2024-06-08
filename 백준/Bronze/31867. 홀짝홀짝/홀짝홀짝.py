n = int(input())
k = int(input())

def solution(n, k):
    odd, even = 0, 0
    for x in str(k):
        if int(x) % 2 != 0:
            odd += 1
        else:
            even += 1
            
    if odd > even:
        return 1
    if odd < even:
        return 0
    
    return -1

print(solution(n, k))