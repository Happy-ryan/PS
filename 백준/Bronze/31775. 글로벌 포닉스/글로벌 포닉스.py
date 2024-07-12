rows = [list(input()) for _ in range(3)]

l, k, p = 0, 0, 0
for row in rows:
    if row[0] == 'l':
        l += 1
    elif row[0] == 'k':
        k += 1
    elif row[0] == 'p':
        p += 1
        
if l == 1 and k == 1 and p == 1:
    print('GLOBAL')
else:
    print('PONIX')