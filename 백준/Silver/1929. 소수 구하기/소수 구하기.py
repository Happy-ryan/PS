# https://www.acmicpc.net/problem/1929

import sys

input = sys.stdin.readline


# 에라토스테네스 체 - 함수
def f(n):
    a = [False, False] + [True] * (n - 1)  # [숫자0,1-소수아님]+[인덱스2~n-소수라고 가정]
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    return primes


M, N = map(int, input().split())

primes_set = f(N)
for x in primes_set:
    if M <= x <= N:
        print(x)