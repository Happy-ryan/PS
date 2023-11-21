# https://www.acmicpc.net/problem/1991
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        dq.appendleft(cmd[1])
    elif cmd[0] == 2:
        dq.append(cmd[1])
    elif cmd[0] == 3:
        if len(dq) != 0:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0] == 4:
        if len(dq) != 0:
            print(dq.pop())
        else:
            print(-1)
    elif cmd[0] == 5:
        print(len(dq))
    elif cmd[0] == 6:
        if len(dq) != 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 7:
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    elif cmd[0] == 8:
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)