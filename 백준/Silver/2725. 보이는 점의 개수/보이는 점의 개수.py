C = int(input())

from math import gcd

memo = [0] * (1001)
# x(분자) / base(분모)
# 중복없는 기울기 = 기약분수 찾기
# 기약분수 = 분자와 분모가 서로소

for base in range(1, 1001):
    for x in range(1, base):
        if gcd(base, x) == 1:
            memo[base] += 1

def solution(N):
    cnt = 3
    for i in range(2, N + 1):
        cnt += memo[i] * 2
    
    return cnt

for _ in range(C):
    N = int(input())
    print(solution(N))