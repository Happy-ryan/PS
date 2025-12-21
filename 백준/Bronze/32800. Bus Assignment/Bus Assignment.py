n = int(input())

cur = 0
ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    cur -= a
    cur += b
    ans = max(ans, cur)

print(ans)