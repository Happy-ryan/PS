N = int(input())

for x in range(1, N+1):
    print(x, end = ' ')
    if x%6 == 0:
        print('Go!', end=' ')
if N%6 != 0:
    print('Go!')