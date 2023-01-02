def solution(s):
    answer = -1
    stack = []
    for x in s:
        if len(stack) == 0:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
    if len(stack) == 0:
        answer = 1
    else: answer = 0
    return answer