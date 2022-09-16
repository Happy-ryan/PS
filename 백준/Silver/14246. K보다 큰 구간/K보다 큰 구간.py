def two_pointer_cnt(data,n,m):

    cnt = 0
    sum = 0
    e = 0
    # ans = []
    for s in range(n):
        while sum <= m and e < n:
            sum += data[e]
            e += 1
        if sum > m:
            cnt += (N-1)-(e-1)+1
            # ans.append((s,e-1))
        sum -= data[s]

    return cnt

N = int(input())
data = list(map(int,input().split()))
M = int(input())

print(two_pointer_cnt(data,N,M))