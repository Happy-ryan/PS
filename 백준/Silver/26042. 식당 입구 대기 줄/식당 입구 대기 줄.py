from collections import deque

n = int(input())
cmds = [list(map(int, input().split())) for _ in range(n)]

def solution(n, cmds):
    waiting = deque([])
    ans_len, ans_last = 0, 0
    
    for cmd in cmds:
        if cmd[0] == 1:
            waiting.append(cmd[1])
        else:
            waiting.popleft()
        
        if waiting:
            if len(waiting) > ans_len:
                ans_len = len(waiting)
                ans_last = waiting[-1]
            elif len(waiting) == ans_len and waiting[-1] < ans_last:
                ans_last = waiting[-1]
    
    return ans_len, ans_last

print(*solution(n, cmds))