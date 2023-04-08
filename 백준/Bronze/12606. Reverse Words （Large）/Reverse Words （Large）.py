t = int(input())
for i in range(1, t + 1):
    row = input().split()[::-1]
    ans = ""
    for s in row:
        ans += " "+s
    print(f"Case #{i}:{ans}")
