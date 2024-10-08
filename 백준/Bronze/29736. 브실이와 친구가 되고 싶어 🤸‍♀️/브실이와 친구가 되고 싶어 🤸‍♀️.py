a, b = map(int, input().split())
k, x = map(int, input().split())

ans = 0
for p in range(a, b + 1):
    if k - x <= p <= k + x:
        ans += 1
        
print(ans if ans != 0 else 'IMPOSSIBLE')