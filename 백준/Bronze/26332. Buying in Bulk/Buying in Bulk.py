N = int(input())
for _ in range(N):
    c, p = map(int, input().split())
    if c == 1:
        print(c, p)
        print(c * p)
    else:
        print(c, p)
        print(c * p - (c - 1)*2)