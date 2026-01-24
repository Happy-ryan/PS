import sys
input = sys.stdin.readline

while True:
    first = input().split()
    if not first:
        break

    d = float(first[0])
    n = int(first[1])

    if d == 0.0 and n == 0:
        break

    hives = [list(map(float, input().split())) for _ in range(n)]
    d2 = d * d

    sour = [False] * n

    for i in range(n):
        x1, y1 = hives[i]
        for j in range(i + 1, n):
            x2, y2 = hives[j]
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= d2:
                sour[i] = True
                sour[j] = True

    sour_count = sum(sour)
    sweet_count = n - sour_count

    print(f"{sour_count} sour, {sweet_count} sweet")
