n = int(input())
s = input()

for x in ["J", "A", "V"]:
    s = s.replace(x, '')

if len(s) == 0:
    print('nojava')
else:
    print(s)