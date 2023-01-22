# x2 : 이진법 특징 문제
def con(n, m):
    res = ''
    conv = '0123456789abcdefghijklmnopqrstuvwxyz'
    if n == 0: return 0
    while n > 0:
        n, mod = divmod(n, m)
        res += conv[mod]
    return res[::-1]
        
def solution(n):
    n = con(n, 2)
    return n.count('1')
    
