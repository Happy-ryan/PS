n, k = map(int, input().split())

def solution(n, k):
    
    def isPrimes(n):
        primes = set()
        a = [False] * 2 + [True] * (n - 1)
        
        for i in range(2, n + 1):
            if a[i]:
                primes.add(i)
                for j in range(i * i, n + 1, i):
                    a[j] = False
                    
        return primes
    
    def isPrime(x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    

    pre = n
    post = n + k * 1000000
    
    if isPrime(pre) and isPrime(post):
        return 'Yes'
    return 'No'
    
print(solution(n, k))