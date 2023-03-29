# https://www.acmicpc.net/problem/15633

# 약수 구하기
def getDivisor(n):
    res = []
    for k in range(1, int(n ** (0.5)) + 1):
        if n % k == 0:
            res.append(k)
            if k**2 != n:
                res.append(n // k)
    res.sort()
    return res


n = int(input())
print(sum(getDivisor(n)) * 5 - 24 )

