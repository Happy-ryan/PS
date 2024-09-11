standard = 1000 

n, m = map(int, input().split())
t = int(input())
for _ in range(t):
    x = int(input())
    res = n * min(standard, x) + m * max(x - standard, 0)
    print(x, res)