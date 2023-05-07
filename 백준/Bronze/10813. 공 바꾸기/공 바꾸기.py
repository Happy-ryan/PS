# https://www.acmicpc.net/problem/10813
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
for _ in range(m):
    idx_a, idx_b = map(int, input().split())
    a, b = arr[idx_a - 1], arr[idx_b - 1]
    arr[idx_a - 1], arr[idx_b - 1] = b, a
    # print(arr)
print(*arr)