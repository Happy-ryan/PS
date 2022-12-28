from itertools import combinations

# 에라토스테네스의 체
def f(n):
    primes = []
    a = [False, False] + [True] * (n - 1)
    
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                a[j] = False
    return primes

def solution(nums):
    answer = 0
    prime_set = set(f(sum(nums)))
    for x, y, z in combinations(nums, 3):
        if x + y + z in prime_set:
            answer += 1
            
    return answer