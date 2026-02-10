s = input()
infos = s.split('(')

if len(infos) == 1:
    print(s)
    print('-')
else:
    print(infos[0])
    print(infos[1][:-1])