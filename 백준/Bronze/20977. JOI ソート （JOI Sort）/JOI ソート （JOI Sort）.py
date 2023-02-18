n = int(input())
s = input()
s = s.replace('J','0')
s = s.replace('I','2')
s = s.replace('O','1')
s = sorted(list(s))
res = ''
for x in s:
    if x == '0':
        res += 'J'
    elif x == '1':
        res += 'O'
    else:
        res += 'I'
print(res)