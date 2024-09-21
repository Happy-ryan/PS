t = int(input())

def solution(s, p):
    time = 0
    post_len = len(s)
    p_len = len(p)
    s = s.replace(p, '')
    pre_len = len(s)
    time += ( post_len - pre_len ) // p_len
    time += pre_len
    
    return time

for _ in range(t):
    s, p = input().split()
    print(solution(s, p))