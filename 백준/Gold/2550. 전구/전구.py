from bisect import bisect_left

n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

lines = []
for i in range(n):
    for j in range(n):
        if left[i] == right[j]:
            lines.append((i, j))
    
lines.sort(key= lambda x: x[0])
stack = []
prev = {}

for i, (l, r) in enumerate(lines):
    idx = bisect_left(stack, (r, -1))
    if idx == len(stack):
        stack.append((r, i))
    else:
        stack[idx] = (r, i)
    if idx > 0:
        prev[i] = stack[idx - 1]

# index
cur = stack[-1][1]
ans = [lines[cur][0]]
while cur in prev:
    cur = prev[cur][1]
    ans.append(lines[cur][0])
    

print(len(ans))
res = []
for x in ans:
    res.append(left[x])
res.sort()
print(*res)