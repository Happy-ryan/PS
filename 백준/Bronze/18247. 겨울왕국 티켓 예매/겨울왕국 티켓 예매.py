def solution(N, M):
    r = ord('L') - ord('A')
    
    if N < 12 or M < 4:
        return -1
    
    r = ord('L') - ord('A')
    
    val = M * r
    
    val += 4
    
    return val

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    print(solution(N, M))