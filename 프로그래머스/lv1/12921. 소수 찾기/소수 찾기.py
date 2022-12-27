def solution(n):
    primes = []
    a = [False, False] + [True] * (n - 1)
        
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                a[j] = False
    
    # print(primes)
    answer = len(primes)
    return answer