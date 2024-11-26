N, M = map(int, input().split())

txt0 = '*.'
txt1 = '.*'

for i in range(N):
    if i % 2 == 0:
        for c in range(M):
            print(txt0[c % 2], end='')
    else:
        for c in range(M):
            print(txt1[c % 2], end='')
    print()
            