n, m = map(int, input().split())
res = [1]
for k in range(2, int(n**(0.5)) + 1):
    if n % k == 0:
        res.append(k)
        if n//k != int(n**(0.5)):
            res.append(n//k)
res.append(n)
res.sort()
# print(res)

if len(res) < m:
    print(0)
else:
    print(res[m - 1])