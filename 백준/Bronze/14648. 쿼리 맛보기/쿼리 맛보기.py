n, q_n = map(int, input().split())
arr = list(map(int, input().split()))

qs = [list(map(int, input().split())) for _ in range(q_n)]

for q in qs:
    if q[0] == 1:
        _, a, b = q
        a -= 1
        b -= 1
        print(sum(arr[a: b + 1]))
        arr[a], arr[b] = arr[b], arr[a]
    else:
        _, a, b, c, d = q
        a -= 1
        b -= 1
        c -= 1
        d -= 1
        print(sum(arr[a: b + 1]) - sum(arr[c: d + 1]))
        