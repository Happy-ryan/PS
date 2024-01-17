# https://www.acmicpc.net/problem/11899

def solution_one(s: str):
    stack = []
    problem_stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                problem_stack.append(x)
    problem_stack.extend(stack)
    return len(problem_stack)

def solution_two(s: str):
    stack = []
    cnt = 0
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                cnt += 1
    cnt += len(stack)
    return cnt

# replace 활용
def solution_three(s: str):
    while '()' in s:
        s = s.replace('()', '')
    return len(s)

s = input()
#print(solution_one(s))
# print(solution_two(s))
print(solution_three(s))