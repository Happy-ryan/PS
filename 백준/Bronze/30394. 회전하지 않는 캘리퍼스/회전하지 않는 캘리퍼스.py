N = int(input())

inf = int(1e18)

min_y = inf
max_y = -inf

for _ in range(N):
    x, y = map(int, input().split())
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print(max_y - min_y)