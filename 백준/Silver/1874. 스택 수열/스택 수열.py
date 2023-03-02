# 자료구조
from collections import deque

n = int(input())
ans = deque([int(input()) for _ in range(n)])
stack = []
res = []

for i in range(1, n + 1):
    if len(stack) == 0:
        stack.append(i)
        res.append('+')
    else:
        while len(stack) != 0 and stack[-1] == ans[0]:
            stack.pop()
            res.append('-')
            ans.popleft()
        stack.append(i)
        res.append('+')

if list(ans) == stack[::-1]:
    for _ in range(len(stack)):
        res.extend('-')
    for x in res:
        print(x)
else:
    print('no'.upper())