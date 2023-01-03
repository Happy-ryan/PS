def f(n, m):
    res = ''
    conv = "0123456789ABCDEF"
    while n > 0:
        n, mod = divmod(n, m)
        res += str(conv[mod])
    return res[::-1]

def solution(n, t, m, p):
    answer = '0'
    res = ''
    for k in range(1, t * m + 1):
        answer += f(k,n)
    cnt = 0
    idx = p - 1
    while cnt != t:
        res += answer[idx]
        idx += m
        cnt += 1
    return res