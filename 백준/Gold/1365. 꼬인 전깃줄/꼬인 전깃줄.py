from bisect import bisect_left

n = int(input())
# 왼쪽 전봇대의 순서대로 정렬이 된 상태이다.
right_lines = list(map(int, input().split()))

stack = []
prev = {}

for i, line in enumerate(right_lines):
    idx = bisect_left(stack, (line, -1))
    if len(stack) == idx:
        stack.append((line, i))
    else:
        stack[idx] = (line, i)
    if idx > 0:
        prev[i] = stack[idx - 1]
        
# print(n - len(stack))
# print(prev)
cur = stack[-1][1]
ans = [stack[-1][0]]
while cur in prev:
    cur = prev[cur][1]
    ans.append(right_lines[cur])
print(n - len(ans))
# 트리
# (2, 0) || (1, 3)
# (3, 1) ||
# (4, 2) ||