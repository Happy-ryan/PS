# https://www.acmicpc.net/problem/2504

def correct_stack(s):
    stack = []
    for x in s:
        if x == '(' or x == '[':
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            if x == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif x == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    if len(stack) != 0:
        return False
    return True

def cal(s):
    stack = []
    for x in s:
        if x == "(" or x == "[":
            stack.append(x)
        else:
            if x == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(2)
                # stack[-1]이 숫자인 경우!
                else:
                    tmp = 0
                    for x in stack[::-1]:
                        if x == '(':
                            break
                        tmp += x
                        stack.pop()
                    stack.pop()
                    stack.append(tmp * 2)
            elif x == ']':
                if stack[-1] == '[':
                    stack.pop()
                    stack.append(3)
                else:
                    tmp = 0
                    for x in stack[::-1]:
                        if x == '[':
                            break
                        tmp += x
                        stack.pop()
                    stack.pop()
                    stack.append(tmp * 3)
    return sum(stack)


s = input()
if correct_stack(s):
    print(cal(s))
else:
    print(0)