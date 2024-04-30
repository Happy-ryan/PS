from collections import deque

n = int(input())
Ss = [deque(list(input().split())) for _ in range(n)]
L = list(input().split())

def solution(n, Ss, L):
    
    for l in L:
        is_exist = False
        for idx in range(n):
            s = Ss[idx]
            # print(s, "s", l, "l")
            if len(s) != 0 and s[0] == l:
                s.popleft()
                is_exist = True
                break
        if not is_exist:
            return 'Impossible'
        
    for s in Ss:
        if len(s) != 0:
            return 'Impossible'
    
    return 'Possible'

print(solution(n, Ss, L))