# https://www.acmicpc.net/problem/2352
from bisect import bisect_left

n = int(input())
ports = list(map(int, input().split()))

stack = []
prev = {}

for i, port in enumerate(ports):
    idx = bisect_left(stack, (port, -1))
    if len(stack) == idx:
        stack.append((port, i))
    else:
        stack[idx] = (port, i)
    if idx > 0:
        prev[i] = stack[idx - 1]
        
# 인덱스
cur = stack[-1][1]
# 값
ans = [stack[-1][0]]
while cur in prev:
    cur = prev[cur][1]
    ans.append(ports[cur])

print(len(stack))
# print(ans)