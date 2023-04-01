# https://www.acmicpc.net/problem/14914
import math


def GetDivisor(n):
    divisor = []
    
    for i in range(1, int(n ** (0.5)) + 1): 
        if n % i == 0:
            divisor.append(i)
            if i * i != n:
                divisor.append(n // i)
    divisor.sort()      
    return divisor

a, b = map(int, input().split())
GCD_ab = math.gcd(a, b)

ans = []
for x in GetDivisor(GCD_ab):
    print(*(x, a//x, b//x))