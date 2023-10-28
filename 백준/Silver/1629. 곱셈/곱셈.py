# https://www.acmicpc.net/problem/1629

A, B, C = map(int, input().split())

# a^x
# Quick power
# (a, 13)
def power(a, x: int, mod):
    ret = 1
    while x:
        # log(x)
        # 1101 & 0001 -> 0001 a^1(0)
        # 110 & 001 -> 000 a^2
        # 11 & 01 -> 01 a^4(0)
        # 1 & 1 -> 1 a^8(0)
        if (x & 1) == 1:
            ret *= a
            ret %= mod
        x >>= 1
        a **= 2
        a %= mod
    return ret

print(power(A, B, C))