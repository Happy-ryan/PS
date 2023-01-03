N, M = map(int, input().split())
def f(n, m):
    res = ''
    while n > 0:
        n, mod = divmod(n, m)
        conv = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res += str(conv[mod])
    return res[::-1]

print(f(N, M))