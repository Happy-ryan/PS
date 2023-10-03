t = int(input())
for _ in range(t):
    A, B, X = map(int, input().split())
    print(A * (X - 1) + B)