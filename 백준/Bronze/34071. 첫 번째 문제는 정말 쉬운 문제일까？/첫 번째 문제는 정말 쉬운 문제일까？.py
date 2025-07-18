n = int(input())
X = [int(input()) for _ in range(n)]

min_x, max_x = min(X), max(X)

if X[0] == min_x:
    print('ez')
elif X[0] == max_x:
    print('hard')
else:
    print('?')