N, K = map(int, input().split())

need = 2 ** (N - 1)

print(K // need)