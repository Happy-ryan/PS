n = int(input())
s = list(input())

dic = {'B': s.count('B'), 'S': s.count('S'), 'A': s.count('A')}
ans = 0
max_value = max(dic.values())
for key, value in dic.items():
    if max_value == value:
        ans += 1

if ans >= 3:
    print('SCU')
else:
    if dic['B'] >= max_value:
        print('B', end='')
    if dic['S'] >= max_value:
        print('S', end='')
    if dic['A'] >= max_value:
        print('A', end='')