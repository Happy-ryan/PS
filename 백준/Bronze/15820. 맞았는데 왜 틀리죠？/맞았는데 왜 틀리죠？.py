s1, s2 = map(int, input().split())
samples = [list(map(int, input().split())) for _ in range(s1)]
systems = [list(map(int, input().split())) for _ in range(s2)]

def solution(s1, s2, samples, systems):
    sam_flag, sys_flag = True, True
    
    for a1, a2 in samples:
        if a1 != a2:
            sam_flag = False

    for a1, a2 in systems:
        if a1 != a2:
            sys_flag = False
            
    if not sam_flag:
        return 'Wrong Answer'
    else:
        if sys_flag:
            return 'Accepted'
        else:
            return 'Why Wrong!!!'

print(solution(s1, s2, samples, systems))