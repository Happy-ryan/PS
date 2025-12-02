import sys
input = sys.stdin.readline

t = int(input())

def conv(n, m):
    if n == 0:
        return 0
    res = ''
    conv = '0123456789abcdef'
    while n > 0:
        n, mod = divmod(n, m)
        res += conv[mod]
    return res[::-1]

for _ in range(t):
    n = int(input())
    print(conv(n, 3))