from fractions import Fraction
from itertools import product, permutations

a, b, c, d = map(int, input().split())

# a / b + c / d <- 현재 a b c d에서 적절히 변경했을 때 두 분수의 합의 최솟값
# 전체 경우의 수 4!
inf = int(1e18)
cnt = inf
answer = (a, b, c, d)
for row in permutations([a, b, c, d]):
    a, b, c, d = row
    P1 = Fraction(a, b)
    P2 = Fraction(c, d)
    P3 = P1 + P2
    if cnt > P3:
        cnt = P3
        answer = (a, b, c, d)
    
# print(cnt)
print(*answer)