N = int(input())
flowers = list(map(int, input().split()))
Q = int(input())
Qs = [list(map(int, input().split())) for _ in range(Q)]


for Q in Qs:
    if Q[0] == 1:
        cnt = 0
        _, l, r, k = Q
        for i in range(l - 1, r):
            if flowers[i] == k:
                cnt += 1
        print(cnt)
    else:
        _, l, r = Q
        for i in range(l - 1, r):
            flowers[i] = 0