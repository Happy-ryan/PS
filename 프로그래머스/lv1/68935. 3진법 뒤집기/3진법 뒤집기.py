# 10진법 n을 m진법으로 변환하는 함수
def f(n, m):
    res = ''
    while n > 0:
        n, mod = divmod(n, m)
        res += str(mod)
    return res[::-1]    
# m진법으로 표현된 n을 10진수로 변환하는 함수
def g(n,m):
    res = 0
    for i in range(len(n)):
        res += int(n[i]) * (m **(len(n) - i - 1))
    return res

def solution(n):
    answer = 0
    f1 = f(n, 3)[::-1]
    answer =g(f1,3)
    return answer