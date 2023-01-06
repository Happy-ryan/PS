from itertools import permutations

def f(n):
    primes = []
    a = [False, False] + [True] * (n - 1)
    
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                a[j] = False
    return primes

def solution(numbers):
    answer = 0
    num_set = set()
    for l in range(1, len(numbers) + 1):
        for row in list(permutations(numbers, l)):
            num_set.add(int(''.join(row)))
    for x in f(max(num_set)):
        if x in num_set: answer += 1
    return answer