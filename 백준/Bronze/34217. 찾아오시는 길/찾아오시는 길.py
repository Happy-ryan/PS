A, B = map(int, input().split())
C, D = map(int, input().split())

if A + C > B + D:
    print('Yongdap')
elif A + C < B + D:
    print('Hanyang Univ.')
else:
    print('Either')