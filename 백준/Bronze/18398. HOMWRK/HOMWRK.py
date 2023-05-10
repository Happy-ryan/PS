T = int(input())
for _ in range(T):
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(a+b, a * b)