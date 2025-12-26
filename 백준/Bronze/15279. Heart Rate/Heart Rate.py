import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    b, p = input().split()
    b = int(b)
    p = float(p)

    min_abpm = 60 * (b - 1) / p
    bpm = 60 * b / p
    max_abpm = 60 * (b + 1) / p

    print(f"{min_abpm:.4f} {bpm:.4f} {max_abpm:.4f}")