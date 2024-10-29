n, d = map(int, input().split())
board = [list(input()) for _ in range(n)]

dic = {'d': ('_', 'q', 'b'),
        'b': ('_', 'p', 'd'),
        'q': ('_', 'd', 'p'),
        'p': ('_', 'b', 'q')}

for row in board:
    for x in row:
        print(dic[x][d], end='')
    print()