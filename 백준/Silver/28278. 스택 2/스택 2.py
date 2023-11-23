# https://www.acmicpc.net/problem/28278
import sys
from collections import deque
input = sys.stdin.readline

stack = deque()
n = int(input())
for _ in range(n):
    cmds = list(map(int, input().split()))
    if cmds[0] == 1:
        stack.append(cmds[1])
    elif cmds[0] == 2:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif cmds[0] == 3:
        print(len(stack))
    elif cmds[0] == 4:
        if len(stack):
            print(0)
        else:
            print(1)
    else:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)