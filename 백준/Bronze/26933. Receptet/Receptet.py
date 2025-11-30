N = int(input())

total = 0

for _ in range(N):
    H, B, K = map(int, input().split())
    if B > H:
        total += (B - H) * K

print(total)
