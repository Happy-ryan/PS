n, m = map(int, input().split())

def f(n, m):
    if n == 0: return 0
    res = ''
    while n > 0:
        conv = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n, mod = divmod(n, m)
        res += str(conv[mod])
    return res[::-1]


print(f(n, m))