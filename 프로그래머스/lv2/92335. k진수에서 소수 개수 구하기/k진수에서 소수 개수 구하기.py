
def prime_check(n):     # n이 소수인지 아닌지 판별
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def f(n, m):
    if n == 0: return '0'
    conv = "0123456789ABCDEF"
    res = ''
    while n > 0:
        n, mod = divmod(n, m)
        res += conv[mod]
    return res[::-1]

def solution(n, k):
    answer = 0
    print(f(n, k))
    for i in f(n, k).split('0'):
        if i.isdigit() and prime_check(int(i)):
            answer += 1
    return answer