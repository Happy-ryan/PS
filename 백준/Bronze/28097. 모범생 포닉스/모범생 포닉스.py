n = int(input())
p = list(map(int, input().split()))
time = sum(p) + (8 * (n-1))

d = time // 24
t = time % 24

print(d, t)