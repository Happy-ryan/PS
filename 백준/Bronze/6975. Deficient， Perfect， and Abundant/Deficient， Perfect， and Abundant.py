# 약수 구하기
def getDivisor(n):
    res = []
    for k in range(1, int(n ** (0.5)) + 1):
        if n % k == 0:
            res.append(k)
            if k**2 != n:
                res.append(n // k)
    res.sort()
    return res[:-1]

n = int(input())
for _ in range(n):
    x = int(input())
    val = sum(getDivisor(x))
    if x == val:
        print(f"{x} is a perfect number." + '\n')
    elif val < x:
        print(f"{x} is a deficient number." + '\n')
    else:
        print(f"{x} is an abundant number." + '\n')