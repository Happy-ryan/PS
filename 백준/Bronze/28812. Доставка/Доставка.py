n, C = map(int, input().split())

inf = 1e18

ans = inf

for _ in range(n):
    p, d, v = map(int, input().split())
    total_cost = p + d + v * C
    ans = min(ans, total_cost)

print(ans)