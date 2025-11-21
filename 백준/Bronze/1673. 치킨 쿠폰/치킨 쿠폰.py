while True:
    try:
        n, k = map(int, input().split())

        total = n
        extra = n

        while extra >= k:
            new = extra // k
            total += new
            extra = extra % k + new

        print(total)

    except:
        break