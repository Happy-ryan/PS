# deque의 rotate 사용
# 자료구조 , deque와 stack
from collections import deque

def stack_check(s):
    stack = []
    
    for i, x in enumerate(s):
        if len(stack) == 0:
            stack.append(x)
        else:
            if stack[-1] == '[' and x == ']':
                stack.pop()
            elif stack[-1] == '(' and x == ')':
                stack.pop()
            elif stack[-1] == '{' and x == '}':
                stack.pop()
            else:
                stack.append(x)
                
    if len(stack) == 0:
        return True
    else:
        return False
        
def solution(s):
    answer = 0
    s = deque(list(s))
    for _ in range(len(s)):
        if stack_check(s):
            answer += 1
        s.rotate(-1)

    return answer