t = int(input())

for _ in range(t):
    N, D, A, B, F = map(float, input().split())
    T = D / (A + B) * F
    print(f"{N} {T:.6f}")