res = []
for i in range(1, 6):
    s = input()
    flag = False
    if 'FBI' in s:
        res.append(i)

if len(res) == 0:
    print('HE GOT AWAY!')
else:
    res.sort()
    print(*res)