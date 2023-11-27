# https://www.acmicpc.net/problem/4134

def isPrime(num: int):
    for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            return True
    return False

def smallestPrime(num):
    while True:
        if num == 0 or num == 1:
            return 2
        if not isPrime(num):
            return num
        num += 1
    
n = int(input())
for _  in range(n):
    num = int(input())
    print(smallestPrime(num))