t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for c in range(1, 51):
        if c != a + b:
            print(c)
            break