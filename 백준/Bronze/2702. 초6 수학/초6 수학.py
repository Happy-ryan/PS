import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print( a * b // math.gcd(a, b), math.gcd(a, b) )