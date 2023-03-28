#  (a2+b2+m)/(ab)

def f(n, m):
    cnt = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            p = (a**2 + b**2 + m) % (a * b)
            if p == 0:
                # print((a**2 + b**2 + m), a*b)
                cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(f(a, b))