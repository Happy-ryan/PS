W = [int(input()) for _ in range(10)]
K = [int(input()) for _ in range(10)]

W.sort()
sum_W = sum(W[-3:])

K.sort()
sum_K = sum(K[-3:])

print(sum_W, sum_K)