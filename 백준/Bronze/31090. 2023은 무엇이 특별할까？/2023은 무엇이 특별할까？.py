n = int(input())
for _ in range(n):
    x = int(input())
    print('Good' if (x + 1) % (x %100) == 0 else 'Bye')