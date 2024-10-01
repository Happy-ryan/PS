s = list(input())
n = int(input())
cmds = [list(input().split()) for _ in range(n)]

def solution(s, n, cmds):
    # L, D, B, P $
    
    # 현재 커서의 위치 맨 마지막!!
    # 커서기준으로 양쪽을 따로 판단
    stack_l = s
    stack_r = []
    
    for cmd in cmds:
        if cmd[0] == 'P':
            stack_l.append(cmd[1])
        elif stack_l and cmd[0] == 'B':
            stack_l.pop()
        elif stack_l and cmd[0] == 'L': 
            x = stack_l.pop()
            stack_r.append(x)
        elif stack_r and cmd[0] == 'D':
            x = stack_r.pop()
            stack_l.append(x)
            

    result = stack_l + stack_r[::-1]
    
    return ''.join(result)

print(solution(s, n, cmds))