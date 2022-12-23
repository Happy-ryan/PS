def solution(s):
    stack = []
    for k in s:
        if len(stack) == 0:
            stack.append(k)
        else:
            if stack[-1] == '(' and k == ')':
                stack.pop()
            else:
                stack.append(k)
    if len(stack) == 0: 
        answer = True
    else : 
        answer = False
    return answer