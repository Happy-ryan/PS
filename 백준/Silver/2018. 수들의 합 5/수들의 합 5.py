def two_pointer_cnt(n):
    data = list(range(1,n+1))

    cnt = 0
    sum = 0
    e = 0

    for s in range(n):
        while sum < n and e < n:
            sum += data[e]
            e += 1
        if sum == n:
            cnt += 1
        sum -= data[s]

    return cnt

N = int(input())
print(two_pointer_cnt(N))