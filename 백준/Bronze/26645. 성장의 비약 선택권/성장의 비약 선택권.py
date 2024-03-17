n = int(input())
ans = []

if 200 <= n <= 209:
    ans.append((1, min(n + 8, 210)))
if 200 <= n <= 219:
    ans.append((2, min(n + 4, 220)))
if 200 <= n <= 229:
    ans.append((3, min(n + 2, 230)))
if 200 <= n <= 239:
    ans.append((4, min(n + 1, 240)))

ans.sort(key= lambda x: (-x[1], -x[0]))

print(ans[0][0])