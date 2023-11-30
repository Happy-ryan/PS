# 10진수 n을 m진수로 변경하는 함수
def conv(n, m):
    if n == 0:
        return 0
    res = ""
    conv = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_@"
    while n > 0:
        n, mod = divmod(n, m)
        res += conv[mod]
    return res[::-1]

def check(n):
    for m in range(2, 65):
        res = conv(n, m)
        if res == res[::-1]:
            return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    print(1 if check(n) else 0)