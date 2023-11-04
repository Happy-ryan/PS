# https://www.acmicpc.net/problem/1009
mod = 10

n = int(input())

def power(a, x):
    ret = 1
    while x:
        if x & 1 == 1:
            ret *= a
            ret %= mod
        x >>= 1
        a **= 2
        a %= mod
    return ret

for _ in range(n):
    a, x = map(int, input().split())
    res = power(a, x)
    if res == 0:
        print(10)
    else:
        print(res)