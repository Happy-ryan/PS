n = int(input())
inf = int(1e8)
ans = inf
for _ in range(n):
    s, e = map(int,input().split())
    if s <= e:
        ans = min(ans, e)

if ans == inf:
    print(-1)
else:
    print(ans)