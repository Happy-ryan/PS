import sys
input = sys.stdin.readline

def conv(n):
    if n == 0:
        return "0"
    res = []
    while n > 0:
        n, mod = divmod(n, 3)
        res.append(str(mod))
    return ''.join(res[::-1])

t = int(input())
for _ in range(t):
    n = int(input())
    print(conv(n))