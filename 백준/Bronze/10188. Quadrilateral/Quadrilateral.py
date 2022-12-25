N = int(input())
for _ in range(N):
    c, r = map(int , input().split())
    for _ in range(r):
        print('X'*c)
    print()