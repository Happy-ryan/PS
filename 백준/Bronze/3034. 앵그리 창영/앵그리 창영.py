N, W, H = map(int, input().split())

d = (W ** 2 + H ** 2) ** 0.5

for _ in range(N):
    l = int(input())
    
    print("DA" if l <= d else "NE")