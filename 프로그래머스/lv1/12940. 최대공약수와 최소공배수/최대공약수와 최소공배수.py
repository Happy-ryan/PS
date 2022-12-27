from math import gcd
def solution(n, m):
    answer = []
    GCD = gcd(n, m)
    LCM = n * m // GCD
    answer = [GCD, LCM]
    return answer