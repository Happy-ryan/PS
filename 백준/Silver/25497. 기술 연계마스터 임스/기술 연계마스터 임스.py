# https://www.acmicpc.net/problem/25497


def solution(s: str):
    cnt = 0
    stack_LR = []
    stack_SK = []
    for x in s:
        if x.isdigit():
            cnt += 1
        elif x == 'L':
            stack_LR.append(x)
        elif x == 'S':
            stack_SK.append(x)
        elif x == 'R':
            if len(stack_LR) == 0:
                return cnt
            stack_LR.pop()
            cnt += 1
        elif x == 'K':
            if len(stack_SK) == 0:
                return cnt
            stack_SK.pop()
            cnt += 1
    return cnt


n = int(input())
s = input()
print(solution(s))