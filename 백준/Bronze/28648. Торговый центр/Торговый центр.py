t = int(input())
inf = int(1e18)

ans = inf

for _ in range(t):
    a, b = map(int, input().split())
    ans = min(ans, a + b)
    
print(ans)