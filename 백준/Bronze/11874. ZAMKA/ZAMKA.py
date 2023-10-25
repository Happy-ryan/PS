# https://www.acmicpc.net/problem/11874
L = int(input())
D = int(input())
X = int(input())

N = D + 1
M = L - 1

def sum_digit(num: int):
    sum_val = 0
    while num > 0:
        sum_val += num % 10
        num //= 10
    return sum_val

for x in range(L, D + 1):
    if sum_digit(x) == X:
        N = min(N, x)
        M = max(M, x)

print(N)
print(M)