N = int(input())

X = list(map(int, input().split()))
L = list(map(int, input().split()))
C = list(input().split())

from itertools import combinations

flag = False
for i, j in combinations(range(0, N), 2):
    if (abs(X[i] - X[j]) <= L[i] + L[j]) and C[i] != C[j]:
        flag = True
        print('YES')
        print(f"{i + 1} {j + 1}")
        break

if not flag:
    print('NO')