N, K = map(int, input().split())

p = 0
max_stand = 0

for _ in range(N):
    a, b = map(int, input().split())
    p -= b
    p += a
    
    stand = max(0, p - K)
    max_stand = max(max_stand, stand)

print(max_stand)