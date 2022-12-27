a, b = map(int, input().strip().split(' '))
answer = ''
for r in range(b):
    for c in range(a):
        print('*', end='')
    print()
        