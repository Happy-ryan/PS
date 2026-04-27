while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    T = [int(input()) for _ in range(n)]
    H = [int(input()) for _ in range(m)]

    sumT = sum(T)
    sumH = sum(H)

    if (sumH - sumT) % 2 != 0:
        print(-1)
        continue

    diff = (sumH - sumT) // 2

    Hset = set(H)

    ans = None

    for a in T:
        b = a + diff
        if b in Hset:
            if ans is None or a + b < sum(ans):
                ans = (a, b)

    if ans:
        print(ans[0], ans[1])
    else:
        print(-1)