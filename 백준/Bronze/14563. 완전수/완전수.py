def getDivisor(n):
    res = []
    for k in range(1, int(n ** (0.5)) + 1):
        if n % k == 0:
            res.append(k)
            if k**2 != n:
                res.append(n // k)
    res.sort()
    return res

t = int(input())
cases = list(map(int, input().split()))
for i in range(t):
    if cases[i] == sum(getDivisor(cases[i])[:-1]):
        print("Perfect")
    elif cases[i] > sum(getDivisor(cases[i])[:-1]):
        print("Deficient")
    else:
        print("Abundant")