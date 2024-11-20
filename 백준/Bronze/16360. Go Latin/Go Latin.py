dic = {
    'a': 'as',
    'i': 'ios',
    'y': 'ios',
    'l': 'les',
    'n': 'anes',
    'ne': 'anes',
    'o': 'os',
    'r': 'res',
    't': 'tas',
    'u': 'us',
    'v': 'ves',
    'w': 'was'
}

t = int(input())
for _ in range(t):
    x = input()
    if x[-1] in dic:
        print(x[:-1] + dic[x[-1]])
    elif x[-2:] in dic:
        print(x[:-2] + dic[x[-2:]])
    else:
        print(x + 'us')