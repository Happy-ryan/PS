T = int(input())
for _ in range(T):
    N, A, D = map(int, input().split())
    print(N * A + N * D * (N - 1) // 2)