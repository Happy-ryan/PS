# https://www.acmicpc.net/problem/4233
# 소수 구하기
def isPrime(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

# 비트연산 & 제곱
def power(a, p):
    mod = p
    ret = 1
    while p:
        if p & 1 == 1:
            ret *= a
            ret %= mod
        p >>= 1
        a **= 2
        a %= mod
    ret %= mod
    return ret


while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    if not isPrime(p) and power(a, p) == a:
        print("yes")
    else:
        print("no")