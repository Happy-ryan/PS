n, h = map(int, input().split())
arr = list(map(int, input().split()))
total = 0

for a in arr:
    if h >= a:
        total += 1

print(total)
