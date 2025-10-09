t = int(input())

a = 118
p = [False] * 2 + [True] * (a - 1)
primes = []
for i in range(2, a + 1):
    if p[i]:
        primes.append(i)
        for j in range(i * i, a + 1, i):
            p[j] = False

totals = []
l = len(primes)
for i in range(l):
    for j in range(l):
        totals.append(primes[i] + primes[j])
    
for _ in range(t):
    num = int(input())
    print('Yes' if num in totals else 'No')