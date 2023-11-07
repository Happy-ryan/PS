n = int(input())

def isPrime(n: int):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def isPalindrome(n: int):
    if str(n) == str(n)[::-1]:
        return True
    return False

def f(n: int):
    for x in range(n, 10000001):
        if isPrime(x) and isPalindrome(x):
            return x
print(f(n))